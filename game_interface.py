import random


CARD_RANG = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
             11: 'Валет', 12: 'Дама', 13: 'Король', 14: 'Туз'}


class Card:
    def __init__(self, suit, rang):
        self.suit = suit
        self.rang = rang

    def __str__(self):
        return f'{CARD_RANG[self.rang]} {self.suit[0]} '


class Deck:
    def __init__(self):
        self.deck = [Card(suit, rang) for suit in (("пики", 'S'), ("трефы", 'C'), ("червы", 'H'), ("бубны", 'D')) for rang in range(2, 15)]


class Player:
    def __init__(self):
        self.list_card = list()
        self.point = 0

    def get_cards(self):
        if self.list_card:
            return f'{", ".join([CARD_RANG[card.rang] + " "+ card.suit[0] for card in self.list_card])}'
        return f'У вас пока нет ни одной карты\n'

    def add_card(self, deck, num=1):
        for _ in range(num):
            card = random.choice(deck.deck)
            self.list_card.append(card)
            self.point = self.scoring()
            deck.deck.pop(deck.deck.index(card))

    def scoring(self):
        result = 0
        for card in sorted(self.list_card, key=lambda x: x.rang):
            if card.rang < 11:
                result += card.rang
            elif card.rang < 14:
                result += 10
            else:
                if result + 11 > 21:
                    result += 1
                else:
                    result += 11
        return result

class Game():
    def __init__(self):
        self.deck = Deck()
        self.bot = Player()
        self.player = Player()
        self.state = 0
        self.res = 'defeat'

    def start_game(self):
        self.__init__()
        self.state = 1
        self.bot.add_card(self.deck, 2)
        self.player.add_card(self.deck, 2)
        return f'Ваши карты: {self.player.get_cards()}\n '\
                f'Ваш счет: {self.player.point}\nВыберите действие'

    def result_game(self):
        self.state = 2
        if self.player.point > 21:
            result = 'Перебор, вы проиграли...'
        else:
            self.__bots_getting_cards()
            if self.bot.point == self.player.point:
                result = 'Результат игры "НИЧЬЯ"'
                self.res = 'draw'
            elif self.bot.point < self.player.point or self.bot.point > 21:
                result = 'Поздравляем!!! Вы выйграли.'
                self.res = 'win'
            else:
                result = 'Извините, но вы проиграли...'
        return 'Противник набрал очков: {0}\n' \
                'Карты противника: {1}\n'\
               'Вы набрали очков: {2}\n'\
                'Ваши карты: {3} \n{4}'.format(
             self.bot.point, self.bot.get_cards(), self.player.point, self.player.get_cards(), result)

    def take_cards(self):
        self.state = 1
        self.player.add_card(self.deck)
        temp = ''
        if self.player.point > 21:
            self.state = 2
            temp = 'У вас перебор!!!\n'
        return f'{temp}Ваши карты: {self.player.get_cards()}\n '\
                f'Ваш счет: {self.player.point}\nВыберите действие'

    def __bots_getting_cards(self):
        while True:
            if self.bot.point < 17 and (17 - self.bot.point) * 20 >= random.randint(1, 100):
                self.bot.add_card(self.deck)
            else:
                break


