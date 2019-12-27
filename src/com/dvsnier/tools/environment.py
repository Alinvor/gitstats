# -*- coding:utf-8 -*-

import sys
from ..configure.constant import _init


class Sniff(object):
    ''' the sniff '''
    def __init__(self):
        super(Sniff, self).__init__()

    def initialized(self):
        ''' the initialized default dict'''
        _init()


class WatchDog(object):
    ''' the watch dog '''
    def __init__(self):
        super(WatchDog, self).__init__()

    def check_version(self):
        ''' the check environment version that python '''
        if sys.version_info < (2, 6):
            print >> sys.stderr, "Python 2.6 or higher is required for gitstats"
            sys.exit(1)


# the single watchdog
watchDog = WatchDog()

# the default sniff
sniff = Sniff()
