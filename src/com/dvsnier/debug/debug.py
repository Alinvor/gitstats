# -*- coding:utf-8 -*-

import sys

# the mark debug mode
_debug_mode = False


class Debug(object):
    ''' debug '''

    # mark whether to ignore the specified mode that is true
    _ignore = True
    _Flag = 0

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

    def setIgnore(self, ignore):
        ''' the get ignore value '''
        self._ignore = ignore

    def getIgnore(self):
        ''' the get ignore value '''
        return self._ignore

    def setFlag(self, flag):
        ''' the get flag value '''
        self._Flag = flag

    def getFlag(self):
        ''' the get flag value '''
        return self._Flag

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
