import logging
import requests

logger = logging.getLogger(__name__)


class ExternalApiHandlerBase:
    @classmethod
    def post(cls=None, endpoint=None, data=None, headers=None):
        return requests.post(endpoint, headers=headers, json=data)

    @classmethod
    def patch(cls=None, endpoint=None, data=None, headers=None):
        return requests.patch(endpoint, headers=headers, json=data)

    @classmethod
    def put(cls=None, endpoint=None, data=None, headers=None):
        return requests.put(endpoint, headers=headers, json=data)

    @classmethod
    def delete(cls=None, endpoint=None, data=None, headers=None):
        return requests.delete(endpoint, headers=headers, json=data)

    @classmethod
    def get(cls, endpoint=None, params=None, headers=None):
        return requests.get(url=endpoint, params=params, headers=headers)
