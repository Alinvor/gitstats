# -*- coding:utf-8 -*-

import sys

# the mark debug mode
_debug_mode = False


class Debug(object):
    ''' debug '''
    def __init__(self):
        super(Debug, self).__init__()

    def isDebug(self):
        ''' the mark whether the current mode is debug '''
        global _debug_mode
        return _debug_mode

    def setDebug(self, mode):
        ''' the set debug mode '''
        global _debug_mode
        _debug_mode = mode

    def exit(self):
        ''' the system exit '''
        sys.exit(0)

    def inspectionTrue(self):
        ''' detection condition, return identity to true '''
        return True

    def inspectionFalse(self):
        ''' detection condition, return identity to false '''
        return False

    def conditions(self, args):
        ''' detection condition, return identity to args '''
        return args


debug = Debug()
