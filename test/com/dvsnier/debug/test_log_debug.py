# -*- coding:utf-8 -*-

import unittest

import sys
import os
import random

sys.path.append(os.path.join(os.getcwd(), "src"))
sys.path.append(os.path.join(os.getcwd(), "mock"))

from com.dvsnier.debug.log_debug import log


class Test_Log(unittest.TestCase):
    ''' the test log debug '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print
        log.setFlag(log._DEFAULT_FLAG)
        log.setDebug(True)

    def test_tips(self):
        print
        log.tips("the test tips() is succeed.")

    def test_withOpen(self):
        base_dir = os.path.join(os.getcwd(), "log")
        file_name = "test_with_open.log"
        msg = "这是一个测试数据,"
        print
        if not os.path.exists(base_dir):
            try:
                os.makedirs(base_dir)
                print("the create dir(%s) is succeed." % base_dir)
            except OSError as e:
                print(e.message)
            else:
                print("the already files %s." % base_dir)
        msg += str(random.randint(1, 100))
        log.withOpen(base_dir, file_name, msg, mode='w+', ignore=False)
        msg += str(random.randint(1, 100))
        log.withOpen(base_dir, file_name, msg, ignore=False)
        msg += str(random.randint(1, 100))
        # log.withOpen(base_dir, file_name, msg, ignore=True)
        log.withOpen(base_dir, file_name, msg, ignore=False)
        log.tips("the test withOpen() is succeed.")

    def test_output(self):
        msg = "这是一个测试数据"
        print
        log.set_default_log_dir(os.getcwd())
        log.output(msg)
        log.tips("the test output() is succeed.")

    def test_outputWithDir(self):
        msg = "这是一个测试数据,test_outputWithDir"
        print
        current_work_dir = os.path.join(os.getcwd(), "log/test_log")
        log.tips("the current cwd is %s" % current_work_dir)
        log.outputWithDir(current_work_dir, msg)
        log.tips("the test output() is succeed.")

    def test_write(self):
        # base_dir = os.path.join(os.getcwd(), "log")
        file_name = "test_with_open.log"
        msg = "这是一个测试数据,write"
        print
        log.write(file_name, msg)
        # log.write(file_name, msg, ignore=True)
        log.tips("the test write() is succeed.")

    def test_writeToDir(self):
        # relative False
        # base_dir = os.path.join(os.getcwd(), "log")

        # relative True
        base_dir = "log"

        sub_dir = "thread"
        file_name = "test_with_thread_open.log"
        msg = "这是一个测试数据,write"
        print
        log.writeToDir(file_name,
                       msg,
                       mode="a+",
                       baseDir=base_dir,
                       subDir=sub_dir,
                       relative=False)
        # log.writeToDir(
        #     file_name,
        #     msg,
        #     mode="a+",
        #     # baseDir=base_dir,
        #     subDir=sub_dir,
        #     relative=False)
        log.tips("the test writeToDir() is succeed.")

    def test_get_current_time_stamp(self):
        print
        print log.get_current_time_stamp()
        log.tips("the test get_current_time_stamp() is succeed.")

    def test_obtain_time_stamp(self):
        print
        print log.obtain_time_stamp()
        print log.obtain_time_stamp(style="log_%s.log")
        print log.obtain_time_stamp(style="%s.bat", fmt="%Y%m%d_%H%M%S")
        log.tips("the test obtain_time_stamp() is succeed.")

    def test_set_default_log_name(self):
        print
        log.set_default_log_name("test.log")
        self.test_get_default_log_name()
        log.tips("the test set_default_log_name() is succeed.")

    def test_get_default_log_name(self):
        print
        print log.get_default_log_name()
        log.tips("the test get_default_log_name() is succeed.")

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(Test_Log)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
