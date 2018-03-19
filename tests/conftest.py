# -*- coding: utf-8 -*-
# @Author: sijanonly
# @Date:   2018-03-19 13:56:26
# @Last Modified by:   sijanonly
# @Last Modified time: 2018-03-19 13:57:28
import pytest


@pytest.fixture(scope="session")
def valid_token_response():
    return {
        "AuthenticateAPIKeyResult":
        {"SecurityToken": "test_TOKEN",
         "ErrorCode": 1400,
         "Result": True,
         "Message": "Successfully generated securitytoken"}}
