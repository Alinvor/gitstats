# -*- coding:utf-8 -*-

import unittest


class Test_Constant(unittest.TestCase):
    '''the test constant'''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")

    def test_constant(self):
        self.assertEqual("1", "1", "the test fail.")

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(Test_Constant)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
