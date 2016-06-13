__author__ = 'sara'

import quickfix
import threading
from multiprocessing import Process
from time import sleep


class MyFixApplication(quickfix.Application):

    def __init__(self):
        quickfix.Application.__init__(self)
        # self.request_message = None
        self.request_message = []

    def onCreate(self, sessionID):

        quickfix.Session.lookupSession(sessionID).reset()

        self.sessionID = sessionID
        print("create session,the id is " + str(sessionID))

    def onLogon(self, sessionID):

        print("onlogon")



        t = Run(self.request_message, self.sessionID)
        p = Process(target=t.start())
        p.start()

    def onLogout(self, sessionID):
        print("onlogout")

    def toAdmin(self, message, sessionID):
        # pass
        print("send %s to %s" % (str(message), sessionID))

    def toApp(self, message, sessionID):
        # pass
        print("send %s to %s" % (str(message), sessionID))

    def fromAdmin(self, message, sessionID):

        print(str(message))

    def run(self, request):

        # print("run request")
        self.request_message = request

        # quickfix.Session.sendToTarget(request, self.sessionID)

    def fromApp(self, message, sessionID):
        print("fromApp")
        print(str(message))


class Run(threading.Thread):

    def __init__(self, request_messages, sessionID):
        threading.Thread.__init__(self)
        self.sessionID = sessionID
        self.request_messages = request_messages

    def run(self):
        try:

            # quickfix.Session.sendToTarget(self.request_messages[0], self.sessionID)
            # print("--------"+str(self.request_messages))

            for request_message in self.request_messages:
                quickfix.Session.sendToTarget(request_message, self.sessionID)

                sleep(2)
                print("==========="+str(request_message))

        except quickfix.SessionNotFound:
            pass
