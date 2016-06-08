__author__ = 'sara'

import quickfix
import threading
class MyFixApplication(quickfix.Application):

    def __init__(self, access_key, secret_key):
        quickfix.Application.__init__(self)
        self.access_key = access_key
        self.secret_key = secret_key
        self.messageOnLogon = None

    def set_message_onLogon(self, value):
        self.messageOnLogon = value

    def onCreate(self, sessionID):

        quickfix.Session.lookupSession(sessionID).reset()

        self.sessionID = sessionID
        print("create session,the id is " + str(sessionID))

    def onLogon(self, sessionID):

        print("onlogon")

    def onLogout(self, sessionID):
        print("onlogout")

    def toAdmin(self, message, sessionID):
        print("toadmin")
        print(str(message))

    def toApp(self, message, sessionID):
        print("toapp")
        print(str(message))

    def fromAdmin(self, message, sessionID):

        print(str(message))

    def run(self, request):

        quickfix.Session.sendToTarget(request, self.sessionID)

    def fromApp(self, message, sessionID):
        quickfix.Message.onMessage(message)
        print("fromApp")
        print(str(message))


class Run(threading.Thread):

    def __init__(self, messageOnLogon, sessionID):
        threading.Thread.__init__(self)
        self.sessionID = sessionID
        self.messageOnLogon = messageOnLogon

    def run(self):
        try:
            quickfix.Session.sendToTarget(self.messageOnLogon, self.sessionID)

        except quickfix.SessionNotFound:
            pass
