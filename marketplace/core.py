import os
from urllib.parse import urljoin

import requests

from .version import __version__


class MarketPlace:
    """Interact with the MarketPlace platform."""

    def __init__(self, endpoint=None, access_token=None):
        endpoint = endpoint or os.environ.get("MP_HOST", "https://the-marketplace.eu")
        access_token = access_token or os.environ["MP_ACCESS_TOKEN"]

        self.endpoint = endpoint
        self.access_token = access_token

    @property
    def default_headers(self):
        """Generate default headers to be used with every request."""
        return {
            "Accept": "application/json",
            "User-Agent": f"MarketPlace Python SDK {__version__}",
            "Authorization": f"Bearer {self.access_token}",
        }

    @property
    def url_userinfo(self):
        return f"{self.endpoint}/user-service/userinfo"

    def get(self, path, **kwargs):
        kwargs.setdefault("headers", {}).update(self.default_headers)
        full_url = urljoin(self.endpoint, path)
        return requests.get(url=full_url, **kwargs)
