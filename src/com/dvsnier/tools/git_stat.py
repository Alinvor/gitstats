# -*- coding:utf-8 -*-

import getopt
import os
import sys
import time
from ..collector.git_data_collector import GitDataCollector
from ..configure.config import conf
from ..configure.constant import get_time_start
from ..configure.constant import get_exectime_external
from .gnuplot_tool import getgnuplotversion
from ..report.html_report_creator import HTMLReportCreator


class GitStats:
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

        outputpath = os.path.abspath(args[-1])
        rundir = os.getcwd()

        try:
            os.makedirs(outputpath)
        except OSError:
            pass
        if not os.path.isdir(outputpath):
            print 'FATAL: Output path is not a directory or does not exist'
            sys.exit(1)

        if not getgnuplotversion():
            print 'gnuplot not found'
            sys.exit(1)

        print 'Output path: %s' % outputpath
        cachefile = os.path.join(outputpath, 'gitstats.cache')

        data = GitDataCollector()
        data.loadCache(cachefile)

        for gitpath in args[0:-1]:
            print 'Git path: %s' % gitpath

            prevdir = os.getcwd()
            os.chdir(gitpath)

            print 'Collecting data...'
            data.collect(gitpath)

            os.chdir(prevdir)

        print 'Refining data...'
        data.saveCache(cachefile)
        data.refine()

        os.chdir(rundir)

        print 'Generating report...'
        report = HTMLReportCreator()
        report.create(data, outputpath)

        time_end = time.time()
        exectime_internal = time_end - get_time_start()
        print 'Execution time %.5f secs, %.5f secs (%.2f %%) in external commands)' % (
            exectime_internal, get_exectime_external(),
            (100.0 * get_exectime_external()) / exectime_internal)
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
