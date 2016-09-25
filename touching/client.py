# -*- coding: utf-8 -*-

import requests

__all__ = ['TOUCHING_API_URL_TEST', 'Touching']
__all__ = ['TOUCHING_API_URL_PROD', 'Touching']

TOUCHING_API_URL_TEST = 'http://api­test.touchinga.com/'
TOUCHING_API_URL_PROD = 'http://www.touchingpos.com/'

class Touching(object):
    def __init__(self, token, is_production=False):
        self.token = token

        if is_production == True:
            self.url = TOUCHING_API_URL_PROD
        else:
            self.url = TOUCHING_API_URL_TEST

        requests_session = requests.Session()
        requests_adapters = requests.adapters.HTTPAdapter(max_retries=3)
        requests_session.mount('http://', requests_adapters)
        self.requests_session = requests_session

    class ResponseError(Exception):
        def __init__(self, code=None, message=None):
            self.code = code
            self.message = message

    @staticmethod
    def get_response(response):
        result = response.json()
        return result

    def _get(self, url, payload=None):
        headers = self.get_headers()
        response = self.requests_session.get(url, headers=headers, params=payload)
        return self.get_response(response)

    def get_headers(self):
        return {'Authorization': "Bearer {}".format(self.token)}

    def find_point(self, tel):
        url = "{}/api/v1/milecards".format(self.url)
        payload = {"tel": tel}
        return self._get(url, payload=payload)
