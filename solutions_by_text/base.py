# -*- coding: utf-8 -*-
# @Author: sijanonly
# @Date:   2018-03-15 12:59:25
# @Last Modified time: 2018-07-27 14:26:14

import json

from urllib import parse

import requests

from .handle_exceptions import CustomException


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

    def _post(self, params):
        headers = {'content-type': 'application/json'}
        absolute_url = self.get_full_path()
        return requests.post(absolute_url, data=json.dumps(params), headers=headers)

    def _get(self, params=None):
        absolute_url = self.get_full_path()
        return requests.get(absolute_url, params=params)


class SolutionByTextAPI(SolutionByTextHTTPInterface):
    """
    Base for SolutionByText API
    """

    __base_url = 'https://{}.solutionsbytext.com/SBT.App.SetUp/RSServices/'

    def __init__(self, security_token, org_code, stage='test'):
        if stage not in ['test', 'ui']:
            raise CustomException('Stages must be either "test" or "ui"')
        # self.api_key = api_key
        self.__org_code = org_code
        self.__stage = stage
        self.__security_token = security_token

    @property
    def stage(self):
        """
        """
        return self.__stage

    @property
    def base_url(self):
        """
        Returns API base url
        """
        return self.__base_url.format(self.stage)

    @property
    def security_token(self):
        """
        """

        return self.__security_token

    @property
    def org_code(self):
        """
        """

        return self.__org_code

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

    def post(self, **kwargs):
        """
        Calls BASE _post method
        """
        payload = {
            "securityToken": self.security_token,
            "orgCode": self.org_code,

        }
        payload.update(**kwargs)
        return self._post(
            params=payload
        )

