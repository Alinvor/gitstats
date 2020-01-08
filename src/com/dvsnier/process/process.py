# -*- coding:utf-8 -*-

import os
import subprocess
import sys
import time
from com.dvsnier.configure.constant import ON_LINUX
from com.dvsnier.configure.constant import set_exectime_external
from com.dvsnier.debug.log_debug import log


def getpipeoutput(cmds, quiet=False):
    ''' the get pipe output '''
    # global exectime_external
    exectime_external = 0.0
    start = time.time()
    file_name = log.obtain_time_stamp("log_%s.log", "%Y%m%d_%H%M%S_%f")
    task_name = log.obtain_time_stamp(style="task_%s", fmt="%m%d_%H%M")
    log.writeToDir(file_name,
                   msg="the current file name is %s" % file_name,
                   subDir=task_name,
                   ignore=False)
    if not quiet and ON_LINUX and os.isatty(1):
        print '>> ' + ' | '.join(cmds),
        sys.stdout.flush()

    log.writeToDir(file_name,
                   msg="the current execute commands: %s" % cmds,
                   subDir=task_name,
                   ignore=False)
    p = subprocess.Popen(cmds[0], stdout=subprocess.PIPE, shell=True)
    processes = [p]
    for x in cmds[1:]:
        log.writeToDir(file_name,
                       msg="the current execute sub commands: %s" % x,
                       subDir=task_name,
                       ignore=False)
        p = subprocess.Popen(x,
                             stdin=p.stdout,
                             stdout=subprocess.PIPE,
                             shell=True)
        processes.append(p)
    output = p.communicate()[0]
    for p in processes:
        p.wait()
    end = time.time()
    if not quiet:
        if ON_LINUX and os.isatty(1):
            print '\r',
        print '[%.5f] >> %s' % (end - start, ' | '.join(cmds))
    exectime_external += (end - start)
    set_exectime_external(exectime_external)
    log.writeToDir(
        file_name,
        msg="the total time spent executing the current command(%s) is %s s." %
        (cmds, str(exectime_external)),
        subDir=task_name,
        ignore=False)
    return output.rstrip('\n')
