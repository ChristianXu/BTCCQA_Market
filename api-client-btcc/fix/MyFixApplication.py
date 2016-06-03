__author__ = 'sara'

import quickfix


class MyFixApplication(quickfix.Application):

    def __init__(self, access_key, secret_key):
        quickfix.Application.__init__(self)
        self.access_key = access_key
        self.secret_key = secret_key

    def onCreate(self, sessionID): return
    def onLogon(self, sessionID): return
    def onLogout(self, sessionID): return
    def toAdmin(self, message, sessionID): return
    def toApp(self, message, sessionID): return
    def fromAdmin(self, message, sessionID): return
    def fromApp(self, message, sessionID): return
