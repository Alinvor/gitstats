# -*- coding:utf-8 -*-

from com.dvsnier.debug.debug import Debug


class Log(Debug, object):
    ''' the log debug '''
    def __init__(self):
        super(Log, self).__init__()

    def v(self, tag, msg):
        if self.isDebug():
            print("[%10s] [%s]" % tag, msg)

    def i(self, tag, msg):
        if self.isDebug():
            print("[%10s] [%s]" % tag, msg)

    def d(self, tag, msg):
        if self.isDebug():
            print("[%10s] [%s]" % tag, msg)

    def w(self, tag, msg):
        if self.isDebug():
            print("[%10s] [%s]" % tag, msg)

    def e(self, tag, msg):
        if self.isDebug():
            print("[%10s] [%s]" % tag, msg)

    def log(self, msg):
        if self.isDebug():
            print("%s" % msg)

    def tips(self, msg):
        print("%s" % msg)


log = Log()
