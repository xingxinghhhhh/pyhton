import unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestLoader().discover("./", "test*.py")
f = open("test01.html", "wb")
runner = HTMLTestRunner(stream=f, title="自动化测试报告",description="Chrome 浏览器")
runner.run(suite)
f.close()