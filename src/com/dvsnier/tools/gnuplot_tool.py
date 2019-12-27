# -*- coding:utf-8 -*-

from ..process.process import getpipeoutput
from ..configure.constant import get_gnuplot_cmd


def getgnuplotversion():
    return getpipeoutput(['%s --version' % get_gnuplot_cmd]).split('\n')[0]
