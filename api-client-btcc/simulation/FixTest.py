__author__ = 'sara'

import os

import quickfix as quickfix

import comm.comm as comm
import fix.MyFixApplication as mfp

fileName = os.path.join(comm.prj_dir, "config", "quickfix-client.properties")

access_key = "1bde6407-836d-46e6-97ee-df368c538bd2"
secret_key = "4560a9b1-6ecf-4724-bffb-bb809a95f2c5"

# try:
settings = quickfix.SessionSettings(fileName)
application = mfp.MyFixApplication(access_key, secret_key)
storeFactory = quickfix.FileStoreFactory(settings)
# logFactory = quickfix.FileLogFactory(settings)

acceptor = quickfix.SocketAcceptor(application, storeFactory, settings)
acceptor.start()
# while condition == true: do something
acceptor.stop()
# except quickfix.ConfigError:

