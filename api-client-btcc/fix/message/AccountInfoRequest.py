#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sara'

import quickfix
import fix.message.field_btcc as field_btcc


class AccountInfoRequest(quickfix.Message):
    """
    账户信息查询
    """

    def __init__(self, account_string, SubAccountInfoRequestType = '1'):
        quickfix.Message.__init__(self)
        self.msg_type = 'U1000'
        self.begin_string = "FIX.4.4"
        self.AccReqID = field_btcc.AccReqID("request009")
        self.SubAccountInfoRequestType = field_btcc.SubAccountInfoRequestType(SubAccountInfoRequestType)
        self.account = quickfix.Account(account_string)
        self.set_request_field()

    def set_request_field(self):
        """
        设置字段
        :return:
        """
        self.getHeader().setField(quickfix.BeginString("FIX.4.4"))
        self.getHeader().setField(quickfix.MsgType(self.msg_type))
        self.setField(self.account)
        self.setField(self.AccReqID)
        self.setField(self.SubAccountInfoRequestType)






