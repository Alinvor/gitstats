# -*- coding:utf-8 -*-

from com.dvsnier.process.process import getpipeoutput
from com.dvsnier.configure.constant import get_gnuplot_cmd

gnuplot_version = ''


def getgnuplotversion():
    ''' the get gnuplot version '''
    global gnuplot_version
    gnuplot_version = getpipeoutput(['%s --version' % get_gnuplot_cmd()])
    print("the current gnuplot version is %s." % gnuplot_version)
    return gnuplot_version.split('\n')[0]
