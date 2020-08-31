# -*- coding:utf-8 -*-

# the mock sys argvs list
_sys_argvs = []

# the test case one
project_name_0 = 'gitstats'
project_path_0 = '../{project_name}'.format(project_name=project_name_0)
project_output_path_0 = './out/{project_name}'.format(
    project_name=project_name_0)
# start_date_0 = '2019-12-26'
# expiry_date_0 = '2020-01-30'
start_date_0 = '2020-01-09'
expiry_date_0 = '2020-01-30'

# the test case two
project_name_1 = 'gitstats'
project_path_1 = '../{project_name}'.format(project_name=project_name_1)
project_output_path_1 = './out/{project_name}'.format(
    project_name=project_name_1)
start_date_1 = '2020-01-07'
expiry_date_1 = '2020-01-30'

# the test case three
project_name_2 = 'iComeKernelAndroidNew'
project_path_2 = '../../Work_Space_Company/{project_name}'.format(
    project_name=project_name_2)
project_output_path_2 = './out/{project_name}'.format(
    project_name=project_name_2)
start_date_2 = '2020-06-01'
expiry_date_2 = '2020-08-31'

# the test case four
project_name_3 = 'iComeKernelAndroidNew'
project_path_3 = '../../Work_Space_Company/{project_name}'.format(
    project_name=project_name_3)
project_output_path_3 = './out/{project_name}'.format(
    project_name=project_name_3)
start_date_3 = '2020-08-01'
expiry_date_3 = '2020-08-31'

sys_argv_0 = [
    '-c', 'start_date={start_date}'.format(start_date=start_date_0), '-e',
    'expiry_date={expiry_date}'.format(expiry_date=expiry_date_0),
    '{project_path}'.format(project_path=project_path_0),
    '{project_output_path}'.format(project_output_path=project_output_path_0)
]

sys_argv_1 = [
    '-c', 'start_date={start_date}'.format(start_date=start_date_1),
    '{project_path}'.format(project_path=project_path_1),
    '{project_output_path}'.format(project_output_path=project_output_path_1)
]

sys_argv_2 = [
    '-c', 'start_date={start_date}'.format(start_date=start_date_2), '-e',
    'expiry_date={expiry_date}'.format(expiry_date=expiry_date_2),
    '{project_path}'.format(project_path=project_path_2),
    '{project_output_path}'.format(project_output_path=project_output_path_2)
]

sys_argv_3 = [
    '-c', 'start_date={start_date}'.format(start_date=start_date_3), '-e',
    'expiry_date={expiry_date}'.format(expiry_date=expiry_date_3),
    '{project_path}'.format(project_path=project_path_3),
    '{project_output_path}'.format(project_output_path=project_output_path_3)
]

_sys_argvs.append(sys_argv_0)
_sys_argvs.append(sys_argv_1)
_sys_argvs.append(sys_argv_2)
_sys_argvs.append(sys_argv_3)


def get_sys_argvs():
    global _sys_argvs
    return _sys_argvs
