__author__ = 'sara'


import quickfix as quickfix
import sys
import comm.comm as comm
import os


fileName = os.path.join(comm.prj_dir, "config", "quickfix-client.properties")

try:
        settings = quickfix.SessionSettings(fileName)
        application = quickfix.Application()
        storeFactory = quickfix.FileStoreFactory(settings)
        logFactory = quickfix.FileLogFactory(settings)
        acceptor = quickfix.SocketAcceptor(application, storeFactory, settings, logFactory)
        acceptor.start()
        # while condition == true: do something
        acceptor.stop()
except quickfix.ConfigError:
        pass
