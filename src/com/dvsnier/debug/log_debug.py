# -*- coding:utf-8 -*-

import os
import datetime
from com.dvsnier.debug.debug import Debug
from com.dvsnier.configure.config import config


class Flag(object):
    ''' the flag '''
    _DEFAULT_FLAG = 0
    _NONE_FLAG = -1


class Log(Debug, Flag, object):
    ''' the log debug '''

    # the default log name
    _default_log_name = ""
    # the default turn off log output
    _log_toggle = False

    def __init__(self):
        super(Log, self).__init__()
        self.set_default_log_name(
            self.obtain_time_stamp("%s.log", fmt="%Y%m%d%H%M%S.%f"))
        self.setFlag(self._NONE_FLAG)

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

    def setDebug(self, mode):
        ''' the set debug mode '''
        super(Log, self).setDebug(mode)
        self.set_log_toggle(not mode)
        return mode

    def log(self, msg):
        if self.isDebug():
            print("%s" % msg)

    def tips(self, msg):
        print("%s" % msg)

    def withOpen(self, base_dir, file_name, msg, mode="a+", ignore=True):
        ''' the write the data to the file in the specified directory,
         debug mode does not write the file '''
        # if self.isDebug() and ignore:
        #     return
        # else:
        #     pass
        if not os.path.exists(base_dir):
            return
        with open(os.path.join(base_dir, file_name), mode) as file:
            if msg:
                file.write("[%s] %s\n" % (self.get_current_time_stamp(), msg))
            else:
                file.write("[%s] the current msg is empty.\n" %
                           self.get_current_time_stamp())

    def output(self, msg):
        ''' the local logging service records '''
        if self.isDebug() and self.getFlag() == self._DEFAULT_FLAG:
            pass
        else:
            return
        self.write(self.get_default_log_name(), msg)

    def write(self, file_name, msg):
        ''' the write data to files that use to append'''
        log_dir = os.path.join(os.getcwd(), "log")
        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
            except OSError:
                pass
        self.withOpen(log_dir, file_name, msg)

    def writeToFile(self, file_name, msg, mode='a+'):
        self.writeToDir(file_name=file_name,
                        msg=msg,
                        mode=mode,
                        baseDir=config.get_current_log_output_path(),
                        subDir=config.get_current_task_name(),
                        relative=False)

    def writeToTempDir(self, msg, mode="a+"):
        self.writeToDir(file_name=config.get_temp(),
                        msg=msg,
                        mode=mode,
                        baseDir=config.get_current_log_output_path(),
                        subDir=config.get_current_task_name(),
                        relative=False)

    def writeToDir(self,
                   file_name,
                   msg,
                   mode="a+",
                   baseDir="log",
                   subDir=None,
                   relative=True):
        ''' the write data to directory files that use to append'''
        if (not log.getIgnore()) and self.getFlag() == self._DEFAULT_FLAG:
            pass
        else:
            return
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
        self.withOpen(cwdir, file_name, msg, mode=mode)

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
        ''' the set default log name '''
        self._default_log_name = log_name

    def get_default_log_name(self):
        ''' the get default log name '''
        return self._default_log_name

    def set_log_toggle(self, toggle):
        ''' the set default log toggle '''
        self._log_toggle = toggle

    def get_log_toggle(self):
        ''' the get default log toggle '''
        return self._log_toggle

    def terminalLog(self):
        ''' turn off log output '''
        # self.setDebug(False)
        self.set_log_toggle(True)


log = Log()
