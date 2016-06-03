__author__ = 'sara'

import quickfix


class AccountInfoRequest(quickfix.Message):

    def __init__(self, account, acc_req_id, sub_account_info_request_type='0'):
        quickfix.Message.__init__(self)
        self.msg_type = 'U1000'
        self.account = account
        self.acc_req_ID = acc_req_id
        self.sub_account_info_request_type = sub_account_info_request_type
        self.set_field()

    def set_field(self):
        self.setField(self.account, self.acc_req_ID, self.sub_account_info_request_type)


