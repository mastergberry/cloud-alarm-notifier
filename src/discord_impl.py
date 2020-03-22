import logging
import json

from os import environ

from src.config import Configuration
from src.utils import make_post_http_request
from src.alarm import Alarm

logger = logging.getLogger()


class DiscordColor:

    RED = 0xFF0000
    YELLOW = 0xFFFF00
    GREEN = 0x00FF00


class DiscordConfiguration(Configuration):

    def __init__(self, remote_type):
        super().__init__(remote_type)

        if 'message' in environ:
            self._message = environ['message']

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        # TODO: Validate 2K character limit
        self._message = message


class DiscordAlarm(Alarm):

    def __init__(self, config):
        # Validate we got the right alarm config
        if not isinstance(config, DiscordConfiguration):
            raise RuntimeError("Invalid configuration given to discord")

        super().__init__(config)

    def send_alarm_message(self, message, timestamp):
        _json = json.loads(message)
        color = DiscordColor.YELLOW
        content = 'Unknown AWS alarm state'
        if 'NewStateValue' in _json:
            if _json['NewStateValue'] == 'ALARM':
                color = DiscordColor.RED
                content = 'AWS alarm raised @everyone :fire: :fire: :fire:'
            elif _json['NewStateValue'] == 'OK':
                color = DiscordColor.GREEN
                content = 'AWS alarm has returned to normal :ok_hand:'

        data = {
            'title': 'AWS Alert',
            'content': content,
            'embeds': [
                {
                    'title': 'AWS Alert',
                    'type': 'rich',
                    'color': color,
                    'timestamp': timestamp,
                    'fields': [
                        {'name': k, 'value': v, 'inline': True} for k, v in _json.items() if isinstance(v, str)
                    ]
                }
            ]
        }

        logger.info('Data being sent %s', data)

        response = make_post_http_request(self.config.url, data)

        logger.info('Response %s', response.read())
