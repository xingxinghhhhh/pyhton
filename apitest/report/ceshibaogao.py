import encodings
import time
import unittest
import sys
sys.path.append(r"C:\\Users\\Administrator\\Desktop\\python1\\apitest")
from script.fff import TestLogin
from HTMLTestRunner import *

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

# report_file = "./report.html".format(time.strftime("%Y%m%d-%H%M%S"))
report_file = "./xixi{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(report_file,"w",encoding="utf8") as f:
    runner=HTMLTestRunner(f,title="嘻嘻嘻")
    runner.run(suite)

