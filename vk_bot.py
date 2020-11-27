#!/usr/bin/env python3
import random
import logging

try:
    import settings
except ImportError:
    exit('DO cp settings.py.default settings.py and set up GROUP_ID and TOKEN vars!')

import vk_api  # TODO fix version!!
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

log = logging.getLogger('bot')


def configure_logging():

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(fmt='%(levelname)s %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('vkbot.log')
    file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%Y %H:%M'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot для vk.com.
    Use Python 3.7
    """
    def __init__(self, group_id, token):
        """

        :param group_id: group_id из группы vk
        :param token: секретный токен из группы vk
        """
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)

        self.api = self.vk.get_api()

    def run(self):
        """Запуск бота."""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события!!! ')

    def on_event(self, event: VkBotEventType):
        """
        Отправлляет сообщение назад, если это текст.

        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            event.object.text = str(event.object.text)
            out_msg = f'Ты сказал: \"{event.object.text.upper()}\", я тебя понял!!!'
            log.debug('Отправляем сообщение назад')
            self.api.messages.send(
                message=out_msg,
                random_id=random.randint(0, 2 ** 20),
                peer_id=event.object.peer_id,
            )
        else:
            log.info('Мы пока не умеем обрабатывать события этого типа %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(group_id=settings.GROUP_ID, token=settings.TOKEN)
    bot.run()
