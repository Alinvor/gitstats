# -*- coding:utf-8 -*-


class ITask(object):
    ''' the task base classes '''
    def __init__(self):
        super(ITask, self).__init__()

    def execute(self):
        ''' the execute task '''
        pass
