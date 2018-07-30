# -*- coding: utf-8 -*-
# @Author: sijanonly
# @Date:   2018-04-02 10:47:46
# @Last Modified by:   sijanonly
# @Last Modified time: 2018-07-27 13:12:18


from .base import SolutionByTextAPI


class SubscriberStatus(SolutionByTextAPI):
    """
    Subscriber status lookup

    Implemention : https://www.solutionsbytext.com/api-support/api-documentation/get-subscribers-status/34/
    """
    service_end_point = 'SubscriberRSService.svc/GetSubscribersStatus'

    def __init__(self, security_token, org_code, stage, phone):
        super().__init__(
            security_token, org_code, stage
        )
        assert not isinstance(phone, list), 'Phone should be list of phone numbers'
        self.phone = phone

    def get(self):
        """
        """
        arg = {
            "phone": self.phone
        }
        return super().get(**arg)


class SubscriberList(SolutionByTextAPI):
    """
    Subscriber list
    """

    service_end_point = 'ReportRSService.svc/Subscribers'

    def __init__(self, security_token, org_code, stage):
        super().__init__(
            security_token, org_code, stage
        )
