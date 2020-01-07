# -*- coding:utf-8 -*-

import os
import datetime
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

    def write(self, file_name, msg, flag=0, ignore=True):
        ''' the write data to files that use to append'''
        if self.isDebug() and ignore:
            return
        else:
            pass
        log_dir = os.path.join(os.getcwd(), "log")
        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
            except OSError:
                pass

        with open(os.path.join(log_dir, file_name), "a+") as file:
            if msg:
                file.write("[%s] %s\n" % (self.get_current_time_stamp(), msg))
            else:
                file.write("[%s] the current msg is empty.\n" %
                           self.get_current_time_stamp())

    def get_current_time_stamp(self):
        ''' the obtain current system datetime '''
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    def obtain_time_stamp(self, style="%s", fmt="%Y%m%d_%H%M%S_%f"):
        ''' the time stamp or get file name
            eg:
                    style              fmt
                log_%s.log      %Y%m%d_%H%M%S_%f
        '''
        if style and style.find("%s") >= 0:
            return (style % datetime.datetime.now().strftime(fmt))
        return datetime.datetime.now().strftime(fmt)


log = Log()
