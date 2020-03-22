from os import environ


class Configuration:

    def __init__(self, remote_type):
        self._remote_type = remote_type

        if 'url' not in environ:
            raise RuntimeError("Missing environment variable 'url'")

        self._url = environ['url']

    @property
    def remote_type(self):
        return self._remote_type

    @remote_type.setter
    def remote_type(self, remote_type):
        self._remote_type = remote_type

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        # TODO: Validate URL
        self._url = url
