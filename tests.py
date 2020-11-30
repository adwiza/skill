from unittest import TestCase
from unittest.mock import patch, Mock, ANY

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

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)
        send_mock = Mock()
        with patch('vk_bot.vk_api.VkApi'):
            with patch('vk_bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)
        send_mock.assert_called_once_with(
            message=self.RAW_EVENT['object']['text'],
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['peer_id'],
        )
