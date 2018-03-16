# -*- coding: utf-8 -*-
# @Author: sijanonly
# @Date:   2018-03-15 12:39:10
# @Last Modified time: 2018-03-15 15:01:30

from .base import SolutionByTextAPI


class CarrierLookUp(SolutionByTextAPI):
    """
    Carrier lookup is the first API call
    """

    service_end_point = 'GeneralRSService.svc/GetCarrierLookup'

    def __init__(self, api_key, org_code, phone):
        super().__init__(
            api_key, org_code,
        )
        self.phone = phone

    def get(self):
        arg = {
            "phone": self.phone
        }
        return super().get(**arg)
