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

if __name__ == '__main__':
    g = GitStats()
    g.run(sys.argv[1:])
