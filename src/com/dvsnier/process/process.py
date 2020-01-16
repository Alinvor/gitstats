# -*- coding:utf-8 -*-

import os
import subprocess
import sys
import time
from com.dvsnier.configure.config import config
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
    if task_name != config.get_current_task_name():
        if config.get_current_task_name():
            log.output(msg="the current task name is now:[%s], old: [%s]" %
                       (task_name, config.get_current_task_name()))
        config.set_current_task_name(task_name=task_name)
    log.writeToDir(file_name,
                   msg="the current file name is %s" % file_name,
                   baseDir=config.get_current_log_output_path(),
                   subDir=task_name,
                   relative=False)
    if not quiet and ON_LINUX and os.isatty(1):
        print '>> ' + ' | '.join(cmds),
        sys.stdout.flush()

    log.writeToDir(file_name,
                   msg="the current execute commands: %s" % cmds,
                   baseDir=config.get_current_log_output_path(),
                   subDir=task_name,
                   relative=False)
    p = subprocess.Popen(cmds[0], stdout=subprocess.PIPE, shell=True)
    processes = [p]
    for x in cmds[1:]:
        log.writeToDir(file_name,
                       msg="the current execute sub commands: %s" % x,
                       baseDir=config.get_current_log_output_path(),
                       subDir=task_name,
                       relative=False)
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
        msg = '[%.5f] >> %s' % (end - start, ' | '.join(cmds))
        print msg
        log.writeToFile(file_name='git_command_script.log', msg=msg)
    exectime_external += (end - start)
    set_exectime_external(exectime_external)
    content = output.rstrip('\n')
    cmd_str = "the total time spent executing the current command[{command}] is {cmd} s.\n"
    content_str = "the execution result is ['{content}']."
    log.writeToDir(file_name,
                   msg=(cmd_str + content_str).format(
                       command=" ".join(cmds),
                       cmd=str(exectime_external),
                       content=content),
                   baseDir=config.get_current_log_output_path(),
                   subDir=task_name,
                   relative=False)
    return content
