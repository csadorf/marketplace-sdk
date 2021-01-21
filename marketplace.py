import os
import requests
from urllib.parse import urljoin


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

    def get(self, path, **kwargs):
        kwargs.setdefault('headers', {}).update(self.default_headers)
        full_url = urljoin(self.endpoint, path)
        return requests.get(url=full_url, **kwargs)
