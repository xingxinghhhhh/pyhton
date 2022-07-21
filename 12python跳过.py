import unittest
version = 35
# @unittest.skip("s")
class my_test1(unittest.TestCase):
    @unittest.skip("代码未完成")
    def test_01(self):
        print("test_01")

    @unittest.skipIf(version <= 30 , "版本大于30才会执行")
    def test_02(self):
        print("test_02")

@unittest.skip("代码未完成")
class my_test2(unittest.TestCase):
    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

unittest.main()
