# -*- coding: utf-8 -*-
# @Author: sijanonly
# @Date:   2018-03-15 12:59:25
# @Last Modified time: 2018-03-15 17:14:29

import json

from urllib import parse

import requests


class CustomException(Exception):
    pass


class SolutionByTextHTTPInterface(object):
    """
    Base class providing interface for actual requests to url.
    """

    def __init__(self, base_url=None, service_end_point=None):
        self.base_url = base_url
        self.service_end_point = service_end_point

    def get_full_path(self):
        """
        Returns full url for service
        """
        return "%s%s" % (self.base_url, self.service_end_point)

    def _post(self, data):
        headers = {'content-type': 'application/json'}
        absolute_url = self.get_full_path()
        return requests.post(absolute_url, data=json.dumps(data), headers=headers)

    def _get(self, params=None):
        absolute_url = self.get_full_path()
        return requests.get(absolute_url, data=json.dumps(params))


class SolutionByTextAPI(SolutionByTextHTTPInterface):
    """
    Base for SolutionByText API
    """

    __base_url = 'https://{}.solutionsbytext.com/SBT.App.SetUp/RSServices/'

    def __init__(self, api_key, org_code, stage='test'):
        if stage not in ['test', 'ui']:
            raise CustomException('Stages must be either "test" or "ui"')
        self.api_key = api_key
        self.org_code = org_code
        self.stage = stage
        self.__security_token = None
        self.__set_security_token()

    def set_security_token(self):
        """
        Calls loginAPI to set security token
        """
        url = ''.join(
            [
                self.base_url,
                'LoginAPIService.svc/AuthenticateAPIKey?',
                parse.urlencode({'APIKey': self.api_key})
            ]
        )

        response_data = json.loads(requests.get(url).text)
        if response_data['AuthenticateAPIKeyResult'].get('ErrorCode') == 1402:
            raise CustomException(
                'Error while authentication. Error in generating security key.')

        self.__security_token = response_data['AuthenticateAPIKeyResult'].get('SecurityToken')

    @property
    def base_url(self):
        """
        Returns API base url
        """
        return self.__base_url.format(self.stage)

    @property
    def security_token(self):
        """
        This method uses the API Key to obtain a Security Token
        """

        return self.__security_token

    def get(self, **kwargs):
        """
        Calls BASE _get method
        """
        payload = {
            "securityToken": self.security_token,
            "orgCode": self.org_code,

        }
        payload.update(**kwargs)
        return self._get(
            params=payload
        )

    __set_security_token = set_security_token   # private copy of original set_security_token() method
