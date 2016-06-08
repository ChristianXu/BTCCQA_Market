__author__ = 'sara'

import os

import quickfix as quickfix

import comm.comm as comm
import fix.MyFixApplication as mfp
import fix.message.AccountInfoRequest as air
import fix.message.field_btcc as fbtcc

fileName = os.path.join(comm.prj_dir, "config", "quickfix-client.properties")

access_key = "cde4ca87-dc34-4a80-af56-01812c66653d"
secret_key = "87f9f8b6-7404-4966-acc4-cceba59f21c5"

account_string = comm.get_account_string(access_key, secret_key)

account = quickfix.Account(account_string)
AccReqID = fbtcc.AccReqID("request009")
SubAccountInfoRequestType = fbtcc.SubAccountInfoRequestType("1")


a = air.AccountInfoRequest(account_string, "1")

# try:
settings = quickfix.SessionSettings(fileName)

application = mfp.MyFixApplication(access_key, secret_key)


storeFactory = quickfix.FileStoreFactory(settings)

# print(storeFactory)
logFactory = quickfix.FileLogFactory(settings)

initiator = quickfix.SocketInitiator(application, storeFactory, settings, logFactory)
print(6)
initiator.block()
# application.run(a)
print(7)
# while condition == true: do something
initiator.stop()
# except quickfix.ConfigError:

