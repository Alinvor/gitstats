# -*- coding:utf-8 -*-

import unittest


class Test_XXX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("...the set up...")

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(Test_XXX)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
