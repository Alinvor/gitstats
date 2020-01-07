# -*- coding:utf-8 -*-

# the mock sys argvs list
_sys_argvs = []

sys_argv_0 = [
    '-c', 'start_date=2019-12-26', '-e', 'expiry_date=2020-01-30',
    '../gitstats', './out/gitstats'
]

sys_argv_1 = ['-c', 'start_date=2019-12-01', '../gitstats', './out/gitstats']

_sys_argvs.append(sys_argv_0)
_sys_argvs.append(sys_argv_1)


def get_sys_argvs():
    global _sys_argvs
    return _sys_argvs
