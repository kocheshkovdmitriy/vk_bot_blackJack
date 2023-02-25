# клавиатуры для чат-бота
# главная клавиатура
# Правила, Играть
keyboard1 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Правила"
                },
                "color": "primary"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Играть"
                },
                "color": "positive"
            }
        ]
    ]
}
# клавиатуры блока ответа
# Взять карту, Вскрываемся
keyboard2 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Взять карту"
                },
                "color": "primary"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Вскрываемся"
                },
                "color": "secondary"
            }
        ]
    ]
}
# Результаты
# Играть снова, Закончить
keyboard3 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Играть снова"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Закончить"
                },
                "color": "primary"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Статистика"
                },
                "color": "positive"
            }
        ]
    ]
}

keyboard = [keyboard1, keyboard2, keyboard3]