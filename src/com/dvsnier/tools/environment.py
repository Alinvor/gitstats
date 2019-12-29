# -*- coding:utf-8 -*-

import sys
from com.dvsnier.configure.constant import _init
from com.dvsnier.process.task import ITask


class Sniff(object):
    ''' the sniff '''
    def __init__(self):
        super(Sniff, self).__init__()

    def initialized(self):
        ''' the initialized default dict'''
        _init()

    def check_version(self):
        ''' the check environment version that python '''
        if sys.version_info < (2, 6):
            print >> sys.stderr, "Python 2.6 or higher is required for gitstats"
            sys.exit(1)

    def transaction(self):
        ''' the transaction process '''
        pass


class WatchDog(ITask, object):
    ''' the watch dog '''
    def __init__(self):
        super(WatchDog, self).__init__()

    def execute(self):
        ''' the execute task list:
            1. the initialized task
            2. the check version
            3. the transaction
            and so on '''
        super(WatchDog, self).execute()
        # ITask.execute(WatchDog, self)
        global _sniff
        _sniff.initialized()
        _sniff.check_version()
        _sniff.transaction()


# the default sniff
_sniff = Sniff()

# the single watchdog
watchDog = WatchDog()
