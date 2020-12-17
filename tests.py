from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY
import settings
from vk_api.bot_longpoll import VkBotMessageEvent

from vk_bot import Bot


class Test1(TestCase):
    RAW_EVENT = {
        'type': 'message_new',
        'object': {'date': 1606715220, 'from_id': 515717314, 'id': 238, 'out': 0, 'peer_id': 515717314,
                   'text': 'Привет бот', 'conversation_message_id': 236, 'fwd_messages': [], 'important': False,
                   'random_id': 0,
                   'attachments': [], 'is_hidden': False},
        'group_id': 200472146,
                   'event_id': '0dc98c8bacc0e4ca20920d94cdcb01ecc10318a6'}

    def test_run(self):
        count = 5
        obj = {'a': 1}
        event = [obj] * count  # [obj, obj, ...]
        long_poller_mock = Mock(return_value=event)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('vk_bot.vk_api.VkApi'):
            with patch('vk_bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    INPUTS = [
        'Привет',
        'А когда?',
        'Где будет конференция?',
        'Зарегистрируй меня',
        'Вениамин',
        'мой адрес email@email',
        'email@email.ru',
    ]
    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.INTENTS[1]['answer'],
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step3']['text'].format(name='Вениамин', email='email@email.ru')
    ]

    def test_run_ok(self):
        send_mock = Mock()
        api_mok = Mock()
        api_mok.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['text'] = input_text
            events.append(VkBotMessageEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('vk_bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot('', '')
            bot.api = api_mok
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        assert real_outputs == self.EXPECTED_OUTPUTS
