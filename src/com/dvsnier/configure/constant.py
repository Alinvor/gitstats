# -*- coding:utf-8 -*-
import os
import platform
import time

os.environ['LC_ALL'] = 'C'

GNUPLOT_COMMON = 'set terminal png transparent size 640,240\nset size 1.0,1.0\n'
ON_LINUX = (platform.system() == 'Linux')
WEEKDAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

exectime_internal = 0.0
exectime_external = 0.0
time_start = time.time()

# By default, gnuplot is searched from path, but can be overridden with the environment variable "GNUPLOT"
gnuplot_cmd = 'gnuplot'


def get_time_start():
    ''' the get time start '''
    global time_start
    return time_start


def get_gnuplot_cmd():
    ''' the get gnuplot command'''
    if 'GNUPLOT' in os.environ:
        global gnuplot_cmd
        gnuplot_cmd = os.environ['GNUPLOT']
    return gnuplot_cmd


def set_exectime_external(exectimeExternal):
    ''' the set exec time external '''
    global exectime_external
    exectime_external = exectimeExternal


def get_exectime_external():
    ''' the get exec time external '''
    global exectime_external
    return exectime_external


def set_exectime_internal(exectimeInternal):
    ''' the set exec time internal '''
    global exectime_internal
    exectime_internal = exectimeInternal


def get_exectime_internal():
    ''' the get exec time internal '''
    global exectime_internal
    return exectime_internal


_global_dict = {}


def _init():
    global _global_dict


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue
