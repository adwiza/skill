#!/usr/bin/env python3

from token import token
import vk_api

group_id = 200472146


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

    def run(self):
        pass


if __name__ == '__main__':
    bot = Bot(group_id, token)
    bot.run()
