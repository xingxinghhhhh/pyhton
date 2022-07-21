import unittest
def my_sum(a,b):
    return a + b

class my_test(unittest.TestCase):
    def test01(self):
        num = my_sum(1,3)
        self.assertEqual(4,num)

    def test02(self):
        num = my_sum(4,3)
        self.assertEqual(4,sum)

    def test03(self):
        num = my_sum(1,2)
        self.assertIn(num,[1,2,3,4,5])

unittest.main()


