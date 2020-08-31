#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Copyright (c) 2007-2014 Heikki Hokkanen <hoxu@users.sf.net> & others (see doc/AUTHOR)
# GPLv2 / GPLv3

import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))
sys.path.append(os.path.join(os.getcwd(), "mock"))

from com.dvsnier.debug.log_debug import log
log.output(msg=("--- start ---"))
log.output(msg=(sys.path))
log.output(msg=("--- end ---"))

# namespace_packages=['dvsnier.gitstat']
from com.dvsnier.tools.git_stat import GitStats

# namespace_packages=['dvsnier.gitstat.mock']
from com.dvsnier.mock.sys_argv import get_sys_argvs


def test_log_mode_0():
    pass


def test_log_mode_1():
    log.setDebug(True)
    log.setIgnore(True)
    log.setFlag(0)


def test_log_mode_2():
    log.setDebug(True)
    log.setIgnore(True)
    log.setFlag(-1)


def test_log_mode_3():
    log.setDebug(True)
    log.setIgnore(False)
    log.setFlag(0)


def test_log_mode_4():
    log.setDebug(True)
    log.setIgnore(False)
    log.setFlag(-1)


def test_log_mode_5():
    log.setDebug(False)
    log.setIgnore(True)
    log.setFlag(0)


def test_log_mode_6():
    log.setDebug(False)
    log.setIgnore(True)
    log.setFlag(-1)


def test_log_mode_7():
    log.setDebug(False)
    log.setIgnore(False)
    log.setFlag(0)


def test_log_mode_8():
    log.setDebug(False)
    log.setIgnore(False)
    log.setFlag(-1)


def test_log_case():
    test_log_mode_0()
    # test_log_mode_1()
    # test_log_mode_2()
    # test_log_mode_3()
    # test_log_mode_4()
    # test_log_mode_5()
    # test_log_mode_6()
    # test_log_mode_7()
    # test_log_mode_8()
    # log.terminalLog()


# the test case
if __name__ == '__main__':

    # test_log_mode_1()
    test_log_mode_3()

    g = GitStats()
    sys_argvs = get_sys_argvs()
    # log.printObject(sys_argvs)
    g.run(sys_argvs[0])
    # g.run(sys_argvs[1])
    # g.run(sys_argvs[2])
    # g.run(sys_argvs[3])
