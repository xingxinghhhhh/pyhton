import unittest
import requests
import sys
sys.path.append(r"C:\\Users\\Administrator\\Desktop\\python1\\apitest")

from requests import session
from api.ppp import aaa


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = aaa()
    
    def setup(self):
        self.session = session()

    def teardowm(self):
        self.session.close()

    def ccc(self):
        response = self.login_api.bbb("student10","123456",False)
        result = response.json()
        print(response)
        self.assertEqual(None,result.get("id"))
        self.assertEqual(200, response.status_code)
        self.assertIn("成功",result.get("message"))

