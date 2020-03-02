# -*- coding:utf-8 -*-

# the mock sys argvs list
_sys_argvs = []
project_name = 'gitstats'
start_date = '2019-12-26'
expiry_date = '2020-01-30'

sys_argv_0 = [
    '-c', 'start_date={start_date}'.format(start_date=start_date), '-e',
    'expiry_date={expiry_date}'.format(expiry_date=expiry_date),
    '../{project}'.format(project=project_name),
    './out/{project}'.format(project=project_name)
]

sys_argv_1 = [
    '-c', 'start_date={start_date}'.format(start_date=start_date),
    '../{project}'.format(project=project_name),
    './out/{project}'.format(project=project_name)
]

_sys_argvs.append(sys_argv_0)
_sys_argvs.append(sys_argv_1)


def get_sys_argvs():
    global _sys_argvs
    return _sys_argvs
