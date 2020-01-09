# -*- coding:utf-8 -*-

conf = {
    'max_domains': 10,
    'max_ext_length': 10,
    'style': 'gitstats.css',
    'max_authors': 20,
    'authors_top': 5,
    'commit_begin': '',
    'commit_end': 'HEAD',
    'linear_linestats': 1,
    'project_name': '',
    'processes': 8,
    'start_date': '',
    'expiry_date': ''
}

# the default log directory
_LOG_DIRECTORY = "log"

# the temporary files
_temporary = "temp"


class Config(object):
    ''' the global config data '''

    # the default html output result path
    _output_path = None
    # the project path
    _project_path = None
    # the current log output result path
    _current_log_output_path = None
    # the current project run path
    _current_run_path = None
    # the current cache path
    _current_cache_path = None
    # the current task name with task pools
    _current_task_name = None

    def __init__(self):
        super(Config, self).__init__()

    def set_output_path(self, output):
        ''' the set current output path '''
        self._output_path = output

    def get_output_path(self):
        ''' the get current output path '''
        return self._output_path

    def set_project_path(self, project_path):
        ''' the set current project path '''
        self._project_path = project_path

    def get_project_path(self):
        ''' the get current project path '''
        return self._project_path

    def set_current_log_output_path(self, output):
        ''' the set current output path '''
        self._current_log_output_path = output

    def get_current_log_output_path(self):
        ''' the get current output path '''
        return self._current_log_output_path

    def set_current_run_path(self, run_path):
        ''' the set current run path '''
        self._current_run_path = run_path

    def get_current_run_path(self):
        ''' the get current run path '''
        return self._current_run_path

    def set_current_cache_path(self, cache_path):
        ''' the set current cache path '''
        self._current_cache_path = cache_path

    def get_current_cache_path(self):
        ''' the get current cache path '''
        return self._current_cache_path

    def set_current_task_name(self, task_name):
        ''' the set current task name with task pools '''
        self._current_task_name = task_name

    def get_current_task_name(self):
        ''' the get current task name with task pools '''
        return self._current_task_name

    def get_log(self):
        ''' the get default log directory name '''
        global _LOG_DIRECTORY
        return _LOG_DIRECTORY

    def get_temp(self):
        ''' the get temporary directory name '''
        global _temporary
        return _temporary


config = Config()
