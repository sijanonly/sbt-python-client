# -*- coding: utf-8 -*-
# @Author: sijanonly
# @Date:   2018-03-16 17:43:21
# @Last Modified by:   sijanonly
# @Last Modified time: 2018-03-19 13:57:23

import requests
import responses
from urllib import parse
import pytest

from solutions_by_text import create_security_token, carrier


_base_url = 'https://{}.solutionsbytext.com/SBT.App.SetUp/RSServices/'


@responses.activate
def test_create_security_token(valid_token_response):

    API_KEY = 'TESTKEY'
    STAGE = 'test'

    url = ''.join(
        [
            _base_url.format(STAGE),
            'LoginAPIService.svc/AuthenticateAPIKey?',
            parse.urlencode({'APIKey': API_KEY})
        ]
    )

    responses.add(responses.GET, url,
                  json=valid_token_response)

    token = create_security_token(API_KEY, STAGE)

    assert token == "test_TOKEN"


@responses.activate
def test_create_security_token_with_wrong_apikey_raises_exception():

    API_KEY = 'TESTKEY'
    STAGE = 'test'

    url = ''.join(
        [
            _base_url.format(STAGE),
            'LoginAPIService.svc/AuthenticateAPIKey?',
            parse.urlencode({'APIKey': API_KEY})
        ]
    )

    responses.add(responses.GET, url,
                  body=Exception('...'))

    with pytest.raises(Exception):
        create_security_token(API_KEY, STAGE)
