import logging

from os import environ
from src.config import Configuration
from src.alarm import Alarm
from src.discord_impl import DiscordConfiguration, DiscordAlarm

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_config():
    if 'remote_type' not in environ:
        raise RuntimeError("Missing environment variable 'remote_type'")

    remote_type = environ['remote_type']
    if remote_type is None:
        raise RuntimeError("Missing environment variable 'remote_type'")

    if remote_type == 'discord':
        return DiscordConfiguration(remote_type)

    return Configuration(remote_type)


def get_alarm(config):
    if config.remote_type == 'discord':
        return DiscordAlarm(config)

    return Alarm(config)


def lambda_handler(event, context):
    logger.info('Event %s', event)

    config = get_config()
    if config is None:
        return {
            'statusCode': 500
        }

    logger.info('Remote type found: %s', config.remote_type)

    # Create and get alarm
    alarm = get_alarm(config)
    alarm.send_alarm_message(event['Records'][0]['Sns']['Message'], event['Records'][0]['Sns']['Timestamp'])

    logger.info('Alarm raised')

    return {
        'statusCode': 200
    }