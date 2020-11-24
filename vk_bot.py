#!/usr/bin/env python3
import random

from _token import token
import vk_api
from vk_api import bot_longpoll
import string

group_id = 200472146


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)

        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                print('Получено событие')
                self.on_event(event)
            except Exception as err:
                print(err)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            out_msg = f'Ты сказал: \"{event.object.text.upper()}\", я тебя понял!!!'
            print(out_msg)
            self.api.messages.send(
                message=out_msg,
                random_id=random.randint(0, 2 ** 20),
                peer_id=event.object.peer_id,
            )
        else:
            print('Мы пока не умеем обрабатывать события этого типа', event.type)


if __name__ == '__main__':
    bot = Bot(group_id, token)
    bot.run()
