
class Alarm:

    def __init__(self, config):
        self._config = config

    @property
    def config(self):
        return self._config

    def send_alarm_message(self, message, timestamp):
        raise RuntimeError("Unimplemented")