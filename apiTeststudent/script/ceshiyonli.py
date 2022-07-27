import unittest
from urllib import response
from parameterized import parameterized
import requests
from requests import Session

import sys
sys.path.append(r"C:\\Users\\Administrator\\Desktop\\python1\\apiTeststudent")

from api.login import login_api
from data.shuju import login_data


class Test_Login(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.dengluapi = login_api()

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

# 登录成功
    @parameterized.expand(login_data)
    def test_login_chenggong(self,userName,password,remember):
        response = self.dengluapi.login_user(userName,password,remember)
        result = response.json()
        print(response)

        self.assertEqual(None,result.get("id"))
        self.assertIn("成功",result.get("message"))

# 进入首页
    def test_shouye_success(self):
        response = self.dengluapi.shouye()
        result = response.json()
        print(response)

        self.assertIn("成功",result.get("message"))

unittest.main()