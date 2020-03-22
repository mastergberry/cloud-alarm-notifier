import urllib3
import json


def make_post_http_request(url, data):
    http = urllib3.PoolManager()

    return http.request('POST',
                        url,
                        body=json.dumps(data),
                        headers={'Content-Type': 'application/json'},
                        retries=True)
