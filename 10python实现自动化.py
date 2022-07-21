from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time

class baidutest(unittest.TestCase):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element(By.ID , "kw").clear(0)
        driver.find_element(By.ID , "kw").send_keys("测试")
        driver.find_element(By.ID , "su").click()
        time.sleep(3)
        title=driver.title
        self.assertEqual(title,u"测试_百度搜索")

    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()