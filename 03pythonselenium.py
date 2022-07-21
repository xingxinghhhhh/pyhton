# UI自动化

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from selenium import webdriver
# import random
#创建浏览器对象
# driver=webdriver.Chrome()
# #获取指定页面
# url="https://www.baidu.com"
# driver.get(url)

# class_name定位元素
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# url="https://www.baidu.com"
# driver.get(url)
# driver.find_element(By.CLASS_NAME , "title-content-title").click()
# time.sleep(10)
# driver.quit()

# xpath路径定位元素
# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
# url="http://learn.antcave.club/#/"
# driver.get(url)
# driver.find_element("name","keywords").send_keys("python")
# time.sleep(10)
# driver.find_element("xpath","/html/body/div/div[1]/div/nav/div/div/div[2]/div/div/button").click()
# time.sleep(20)


# CSS里用id定位：#ID
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# url="https://www.baidu.com"
# print(driver.get(url))
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT , "登录").click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR , "#TANGRAM__PSP_11__userName").send_keys("13546465211")
# time.sleep(10)
# driver.quit()

# 使用属性和逻辑来查找元素
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# url="https://www.baidu.com"
# print(driver.get(url))
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT , "登录").click()
# time.sleep(3)
# driver.find_element(By.XPATH , "//input[@type='text' and @name='username']").send_keys("13546465211")
# time.sleep(10)
# driver.quit()


# CSS里用class定位
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# url="https://www.baidu.com"
# print(driver.get(url))
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT , "登录").click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR , "[class='pass-text-input pass-text-input-userName']").send_keys("13546465211")
# time.sleep(10)
# driver.quit()



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# url="https://www.baidu.com"
# print(driver.get(url))
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT , "登录").click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR , "#TANGRAM__PSP_11__userNameWrapper>#TANGRAM__PSP_11__userName").send_keys("13546465211")
# time.sleep(10)
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# url="https://www.baidu.com"
# print(driver.get(url))
# time.sleep(3)
# driver.find_element(By.ID , "kw").send_keys("企查查")
# time.sleep(3)
# driver.find_element(By.ID , "su").click()
# time.sleep(3)
# driver.find_element(By.XPATH , "/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div/div[2]/a").click()
# time.sleep(3)
# windows_handles=driver.window_handles  # 获取所有句柄
# print(windows_handles)
# driver.switch_to.window(windows_handles[-1])   # 切换到最后一个句柄
# time.sleep(5)
# driver.find_element(By.ID , "searchKey").click()
# time.sleep(3)
# driver.find_element(By.XPATH , "/html/body/div/div[2]/section[1]/div/div/div/div[1]/div/div/input").send_keys("百度")
# time.sleep(3)
# driver.find_element(By.CLASS_NAME , "input-group-btn").click()
# time.sleep(3)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.implicitly_wait(20)
# driver.find_element(By.ID , "kw").send_keys("LOL")
# driver.implicitly_wait(20)
# driver.find_element(By.ID , "su").click()
# driver.implicitly_wait(20)
# driver.find_element(By.XPATH , "/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/div/div[1]/h3/a[1]").click()
# driver.implicitly_wait(20)
# driver.switch_to.window(driver.window_handles[0])
# driver.find_element(By.ID , "kw").clear()
# driver.implicitly_wait(20)
# driver.find_element(By.ID , "kw").send_keys("abcd")
# driver.implicitly_wait(20)
# driver.find_element(By.ID , "su").click()
# newwindow = 'window.open("https://www.bilibili.com")'
# driver.execute_script(newwindow)     # 创建一个新的窗口
# driver.maximize_window()   #  最大化窗口
# driver.set_window_size(200,200)  # 设置浏览器窗口大小宽高
# driver.set_window_position(200,200)   # 设置浏览器窗口位置，在桌面的位置
# driver.implicitly_wait(20)   # 隐式等待时间
# driver.back()  # 后退
# driver.forward()  # 前进
# driver.refresh()  # 刷新
# driver.close()  #  关闭当前窗口
# driver.quit()  # 关闭
# print(driver.title)  # 打印标题
# print(driver.current_url)   # 打印当前URL