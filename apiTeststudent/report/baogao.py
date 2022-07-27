import time
import unittest
import sys
sys.path.append(r"C:\\Users\\Administrator\\Desktop\\python1\\apiTeststudent")
from script.ceshiyonli import Test_Login
from HTMLTestRunner import *

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_Login))


report_file = "./report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(report_file,"w",encoding="utf-8") as haha:
    runner = HTMLTestRunner(haha,title="测试报告")
    runner.run(suite)
