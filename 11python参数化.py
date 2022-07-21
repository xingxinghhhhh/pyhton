# 使用@parameterized.expand 装饰器可以为测试函数的参数进行参数化
import unittest
from parameterized import parameterized

def my_sum(a,b):
    return a + b

class testmy_sum(unittest.TestCase):
    @parameterized.expand([(1,1,2),(1,0,1),(0,0,0)])
    def test_01(self,x,y,expect):
        result = my_sum(x,y)
        self.assertEqual(result,expect)

unittest.main()