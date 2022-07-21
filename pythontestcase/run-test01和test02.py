import unittest
import test01
import test02
suite = unittest.TestSuite()
suite.addTest(test01.my_test01("test_01"))
# 添加my_test02类中所有test开头的方法
suite.addTest(unittest.makeSuite(test02.my_test02))
runner = unittest.TextTestRunner()
runner.run(suite)



#  TestLoader 用法
# import unittest
# suite = unittest.TestLoader().discover("./","test*.py")
# suite = unittest.defaultTestLoader.discover("./")   # 搜索在当前文件夹下所有默认以test开头的python文件
# runner = unittest.TextTestRunner()
# runner.run(suite)


