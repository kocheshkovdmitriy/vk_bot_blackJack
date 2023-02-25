import keyboards
from os import environ as env
import vk_api
from vk_api import VkUpload
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import json
from game_interface import Game
from database.core import crud


load_dotenv()  # .env
vk_session = vk_api.VkApi(token=env['VK_TOKEN'])  # токен
longpoll = VkLongPoll(vk_session)  # ID
upload = VkUpload(vk_session)
vk = vk_session.get_api()  # открытие сессии

games = dict()


def get_attachments(list_card):
    if list_card:
        photos = upload.photo_messages(photos=[f'Img/{card.rang}{card.suit[1]}.png' for card in list_card])
        return ['photo{}_{}'.format(photo['owner_id'], photo['id']) for photo in photos]
    return []


def write_message(user_id, message, attachments=[], state=0):
    vk_session.method('messages.send', {
        'user_id': user_id,
        'keyboard': json.dumps(keyboards.keyboard[state], ensure_ascii=True),
        'message': message,
        'attachment': ','.join(attachments),
        'random_id': get_random_id()})


def get_rules():
    with open('rules.txt', 'r', encoding="utf-8") as rules:
        mess = rules.read()
    return mess

def get_statistic(user_id):
    temp = [el[0] for el in crud.read_log(['result_game'], [f'user_id = {user_id}'])]
    win = temp.count('win')
    draw = temp.count('draw')
    defeat = temp.count('defeat')
    return f'Сыграно игр: {len(temp)}\n'\
           f'Из них выйграно: {win}\n' \
           f'Закончилось ничьей: {draw}\n' \
           f'Проиграно: {defeat}'


def run_bot_vk():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            user_id = event.user_id
            if user_id not in games.keys():
                games[user_id] = Game()
            text = event.text.lower()
            print(f'Новое сообщение {event.datetime}: {text} от {user_id}')

            if text in ['привет', 'закончить']:
                games[user_id].state = 0
                write_message(user_id,
                              'Привет, сыграем?',
                              state=games[user_id].state)
            elif text == 'правила':

                write_message(user_id,
                              get_rules(),
                              state=games[user_id].state)
            elif text in ['играть', 'играть снова']:
                write_message(user_id,
                              games[user_id].start_game(),
                              get_attachments(games[user_id].player.list_card),
                              state=games[user_id].state)
            elif text == 'взять карту':
                write_message(user_id,
                              games[user_id].take_cards(),
                              get_attachments(games[user_id].player.list_card),
                              state=games[user_id].state)
                if games[user_id].player.point > 21:
                    crud.write_log(user_id, event.datetime, games[user_id].res)
            elif text == 'вскрываемся':
                write_message(user_id,
                              games[user_id].result_game(),
                              state=games[user_id].state)
                crud.write_log(user_id, event.datetime, games[user_id].res)
            elif text == 'статистика':
                write_message(user_id,
                              get_statistic(user_id),
                              state=games[user_id].state)
            else:
                write_message(user_id,
                              'Я вас не понял, повторите ваш выбор',
                              state=games[user_id].state)


if __name__ == '__main__':
    run_bot_vk()