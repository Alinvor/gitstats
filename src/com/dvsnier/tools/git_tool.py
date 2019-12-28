# -*- coding:utf-8 -*-

import os
import re
from com.dvsnier.process.process import getpipeoutput
from com.dvsnier.configure.config import conf


def getgitversion():
    ''' the git version '''
    return getpipeoutput(['git --version']).split('\n')[0]


def getnumoffilesfromrev(time_rev):
    """ Get number of files changed in commit """
    time, rev = time_rev
    return (int(time), rev,
            int(
                getpipeoutput(
                    ['git ls-tree -r --name-only "%s"' % rev,
                     'wc -l']).split('\n')[0]))


def getnumoflinesinblob(ext_blob):
    """ Get number of lines in blob """
    ext, blob_id = ext_blob
    return (ext, blob_id,
            int(
                getpipeoutput(['git cat-file blob %s' % blob_id,
                               'wc -l']).split()[0]))


VERSION = 0


def getversion():
    ''' the get version '''
    global VERSION
    if VERSION == 0:
        gitstats_repo = os.path.dirname(os.path.abspath(__file__))
        VERSION = getpipeoutput([
            "git --git-dir=%s/.git --work-tree=%s rev-parse --short %s" %
            (gitstats_repo, gitstats_repo,
             getcommitrange('HEAD').split('\n')[0])
        ])
    return VERSION


def getlogrange(defaultrange='HEAD', end_only=True):
    ''' the get log range '''
    commit_range = getcommitrange(defaultrange, end_only)
    if len(conf['start_date']) > 0:
        return '--since="%s" "%s"' % (conf['start_date'], commit_range)
    return commit_range


def getcommitrange(defaultrange='HEAD', end_only=False):
    ''' the get commit range '''
    if len(conf['commit_end']) > 0:
        if end_only or len(conf['commit_begin']) == 0:
            return conf['commit_end']
        return '%s..%s' % (conf['commit_begin'], conf['commit_end'])
    return defaultrange


def getkeyssortedbyvalues(dict):
    ''' the get keys soirted by values '''
    return map(lambda el: el[1],
               sorted(map(lambda el: (el[1], el[0]), dict.items())))


# dict['author'] = { 'commits': 512 } - ...key(dict, 'commits')
def getkeyssortedbyvaluekey(d, key):
    ''' the get keys sorted by value key '''
    return map(lambda el: el[1],
               sorted(map(lambda el: (d[el][key], el), d.keys())))


def getstatsummarycounts(line):
    ''' the get stat summary counts '''
    numbers = re.findall('\\d+', line)
    if len(numbers) == 1:
        # neither insertions nor deletions: may probably only happen for "0 files changed"
        numbers.append(0)
        numbers.append(0)
    elif len(numbers) == 2 and line.find('(+)') != -1:
        numbers.append(0)
        # only insertions were printed on line
    elif len(numbers) == 2 and line.find('(-)') != -1:
        numbers.insert(1, 0)
        # only deletions were printed on line
    return numbers
