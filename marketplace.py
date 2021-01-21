import os
import requests


class MarketPlace:

    def __init__(self, endpoint=None, access_token=None):
        if endpoint is None:
            endpoint = os.environ['MARKETPLACE_ENDPOINT']
        if access_token is None:
            access_token = os.environ.get('MARKETPLACE_TOKEN')

        self.endpoint = endpoint
        self.access_token = access_token

    @property
    def default_headers(self):
        return {
                  "Accept": "application/json",
                  "User-Agent": "JupyterNotebook",
                  "Authorization": f"Bearer {self.access_token}",
               }

    @property
    def url_userinfo(self):
        return f'{self.endpoint}/user-service/userinfo'

    def get(self, url, **kwargs):
        kwargs.setdefault('headers', {}).update(self.default_headers)
        return requests.get(url=url, **kwargs)
