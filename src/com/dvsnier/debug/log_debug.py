# -*- coding:utf-8 -*-

import os
import datetime
from com.dvsnier.debug.debug import Debug
from com.dvsnier.configure.config import config


class Log(Debug, object):
    ''' the log debug '''

    _default_log_name = ""

    def __init__(self):
        super(Log, self).__init__()
        self.set_default_log_name(
            self.obtain_time_stamp("%s.log", fmt="%Y%m%d%H%M%S.%f"))

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

    def withOpen(self, base_dir, file_name, msg, mode="a+", ignore=True):
        ''' the write the data to the file in the specified directory,
         debug mode does not write the file '''
        if self.isDebug() and ignore:
            return
        else:
            pass
        if not os.path.exists(base_dir):
            return
        with open(os.path.join(base_dir, file_name), mode) as file:
            if msg:
                file.write("[%s] %s\n" % (self.get_current_time_stamp(), msg))
            else:
                file.write("[%s] the current msg is empty.\n" %
                           self.get_current_time_stamp())

    def output(self, msg, flag=0, ignore=False):
        ''' the local logging service records '''
        self.write(self.get_default_log_name(), msg, flag, ignore)

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
        self.withOpen(log_dir, file_name, msg, ignore=ignore)

    def writeToTempDir(self, msg, mode="a+", flag=0, ignore=True):
        self.writeToDir(file_name=config.get_temp(),
                        msg=msg,
                        mode=mode,
                        baseDir=config.get_current_log_output_path(),
                        subDir=config.get_current_task_name(),
                        flag=flag,
                        ignore=ignore,
                        relative=False)

    def writeToDir(self,
                   file_name,
                   msg,
                   mode="a+",
                   baseDir="log",
                   subDir=None,
                   flag=0,
                   ignore=True,
                   relative=True):
        ''' the write data to directory files that use to append'''
        if self.isDebug() and ignore:
            return
        else:
            pass
        base_dir = None
        sub_dir = None
        cwdir = None
        if baseDir:
            if relative:
                base_dir = os.path.join(os.getcwd(), baseDir)
            else:
                base_dir = baseDir
            if not os.path.exists(base_dir):
                try:
                    os.makedirs(base_dir)
                except OSError:
                    pass
            cwdir = base_dir
        if subDir:
            sub_dir = os.path.join(base_dir, subDir)
            # if relative:
            #     sub_dir = os.path.join(base_dir, subDir)
            # else:
            #     sub_dir = os.path.join(base_dir, subDir)
            if not os.path.exists(sub_dir):
                try:
                    os.makedirs(sub_dir)
                except OSError:
                    pass
            cwdir = sub_dir
        self.withOpen(cwdir, file_name, msg, mode=mode, ignore=ignore)

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

    def set_default_log_name(self, log_name):
        self._default_log_name = log_name

    def get_default_log_name(self):
        return self._default_log_name


log = Log()
