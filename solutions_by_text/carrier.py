# -*- coding: utf-8 -*-
# @Author: sijanonly
# @Date:   2018-03-15 12:39:10
# @Last Modified time: 2018-04-02 12:10:36

from .base import SolutionByTextAPI


class CarrierLookUp(SolutionByTextAPI):
    """
    Carrier lookup is the first API call

    Implementation : https://www.solutionsbytext.com/api-support/api-documentation/get-carrier-lookup/46/
    """

    service_end_point = 'GeneralRSService.svc/GetCarrierLookup'

    def __init__(self, security_token, org_code, stage, phone):
        super().__init__(
            security_token, org_code, stage
        )
        self.phone = phone

    def get(self):
        """
        """
        arg = {
            "phone": self.phone
        }
        return super().get(**arg)
