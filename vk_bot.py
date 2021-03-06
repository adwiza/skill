#!/usr/bin/env python3
import random
import logging

from pony.orm import db_session

import handlers
from models import UserState, Registration

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
        self.VkBotLongPoll = None
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

    @db_session
    def on_event(self, event):
        """
        Отправлляет сообщение назад, если это текст.

        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('Мы пока не умеем обрабатывать события этого типа %s', event.type)
            return
            # event.object.text = str(event.object.text)
            # out_msg = f'Ты сказал: \"{event.object.text.upper()}\", я тебя понял!!!'
            # log.debug('Отправляем сообщение назад')
        user_id = event.object.peer_id
        text = event.object.text

        state = UserState.get(user_id=str(user_id))

        if state is not None:
            text_to_send = self.continue_scenario(text, state)
        else:
            # search indent
            for intent in settings.INTENTS:
                log.debug(f'User gets {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
                else:
                    text_to_send = settings.DEFAULT_ANSWER

        self.api.messages.send(
            message=text_to_send,
            random_id=random.randint(0, 2 ** 20),
            peer_id=user_id,
        )

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        UserState(user_id=str(user_id), scenario_name=scenario_name, step_name=first_step, context={})
        return text_to_send

    def continue_scenario(self, text, state):

        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        # continue scenario
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            # next step
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                # switch to next step
                state.step_name = step['next_step']
            else:
                # finish scenario
                log.info('Зарегистрирован {name} {email}'.format(**state.context))
                Registration(name=state.context['name'], email=state.context['email'])
                state.delete()
        else:
            # retry current step
            text_to_send = step['failure_text'].format(**state.context)

        return text_to_send


if __name__ == '__main__':
    configure_logging()
    bot = Bot(group_id=settings.GROUP_ID, token=settings.TOKEN)
    bot.run()
