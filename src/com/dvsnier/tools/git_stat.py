# -*- coding:utf-8 -*-

import getopt
import os
import sys
import time
from com.dvsnier.collector.git_data_collector import GitDataCollector
from com.dvsnier.configure.config import conf
from com.dvsnier.configure.config import config
from com.dvsnier.configure.constant import get_time_start
from com.dvsnier.configure.constant import get_exectime_external
from com.dvsnier.debug.log_debug import log
from com.dvsnier.tools.gnuplot_tool import getgnuplotversion
from com.dvsnier.report.html_report_creator import HTMLReportCreator


class GitStats(object):
    def __init__(self):
        super(GitStats, self).__init__()

    def run(self, args_orig):
        optlist, args = getopt.getopt(args_orig, 'hc:e:', ["help"])
        for o, v in optlist:
            if o == '-c' or '-e':
                key, value = v.split('=', 1)
                if key not in conf:
                    raise KeyError('no such key "%s" in config' % key)
                if isinstance(conf[key], int):
                    conf[key] = int(value)
                else:
                    conf[key] = value
            elif o in ('-h', '--help'):
                usage()
                sys.exit()

        if len(args) < 2:
            usage()
            sys.exit(0)
        log.output(msg='Initialized data...')
        outputpath = os.path.abspath(args[-1])
        rundir = os.getcwd()
        config.set_current_run_path(rundir)
        log.output(msg='the current run path: %s' % rundir)
        logdir = os.path.join(rundir, config.get_log())
        config.set_current_log_output_path(logdir)
        log.output(msg='the current log path: %s' % logdir)
        try:
            os.makedirs(outputpath)
        except OSError as e:
            if e.message:
                log.output(e.message)
            else:
                log.output(e)
        if not os.path.isdir(outputpath):
            print 'FATAL: Output path is not a directory or does not exist'
            log.output(
                msg='FATAL: Output path is not a directory or does not exist')
            sys.exit(1)

        if not getgnuplotversion():
            print 'gnuplot not found'
            log.output(msg='gnuplot not found')
            sys.exit(1)
        config.set_output_path(outputpath)
        log.output(msg='the current Output path: %s' % outputpath)
        cachefile = os.path.join(outputpath, 'gitstats.cache')
        config.set_current_cache_path(cachefile)
        log.output(msg='the current cache file path is %s' % cachefile)
        if os.path.exists(cachefile):
            log.output(msg='the current cache file is existence')
        else:
            log.output(msg='the current cache file is not existence')

        data = GitDataCollector()
        data.loadCache(cachefile)

        for gitpath in args[0:-1]:
            abs_git_path = os.path.abspath(gitpath)
            config.set_project_path(abs_git_path)
            log.output('the current project(git) relative path is %s' %
                       gitpath)
            log.output('the current project(git) path is %s' % abs_git_path)

            prevdir = os.getcwd()
            os.chdir(gitpath)

            log.output('Collecting data...')
            data.collect(gitpath)

            os.chdir(prevdir)

        log.output(msg='Refining data...')
        data.saveCache(cachefile)
        data.refine()

        os.chdir(rundir)

        log.output(msg='Generating report...')
        report = HTMLReportCreator()
        report.create(data, outputpath)

        time_end = time.time()
        exectime_internal = time_end - get_time_start()
        msg = 'Execution time %.5f secs, %.5f secs (%.2f %%) in external commands)' % (
            exectime_internal, get_exectime_external(),
            (100.0 * get_exectime_external()) / exectime_internal)
        log.output(msg=msg)
        if sys.stdin.isatty():
            print 'You may now run:'
            print
            print '   sensible-browser \'%s\'' % os.path.join(
                outputpath, 'index.html').replace("'", "'\\''")
            print


def usage():
    print """
Usage: gitstats [options] <gitpath..> <outputpath>

Options:
-c key=value     Override configuration value

Default config values:
%s

Please see the manual page for more details.
""" % conf
