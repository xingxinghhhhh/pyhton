# 方法级别
import unittest
class my_test01(unittest.TestCase):
    def setUp(self):
        print("setup执行")
    def tearDown(self):
        print("teatdown执行")
    def test_01(self):
        print("my_test01的test01")
    def test_02(self):
        print("my_test01的test02")
    
unittest.main()


# 类级别
'''
使用：初始化(前置处理): @classmethod def setUpClass(cls): --> 首先自动执行
销毁(后置处理): @classmethod def tearDownClass(cls): --> 最后自动执行
运 行于 测试 类的 始末 , 即： 每个 测试 类 只会 运行 一次 setUpClass 和
tearDownClass
'''

import unittest
class my_test01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass执行")
    @classmethod
    def tearDownClass(cls):
        print("teardownclass执行")
    def setup(self):
        print("setup执行")
    def teardown(self):
        print("teardown执行")
    def test_01(self):
        print("my_test01的test01")
    def test_02(self):
        print("my_test01的test02")

unittest.main()

