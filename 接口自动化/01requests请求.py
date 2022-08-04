#  安装：pip install requests
#  常见的HTTP请求方式：GET、POST、PUT、DELETE



# 导包
# import requests
# 发送GET请求
# response = requests.get("http://www.baidu.com")


# 发送post请求
# response = requests.post(url, data=None, json=None)
"""
 :param url: 请求的URL
 :param data: (可选) 要发送到请求体中的字典、元组、字节或文件对象
 :param json: (可选) 要发送到请求体中的JSON数据
 :rtype: requests.Response
 """


# import requests
# response = requests.get("http://39.105.34.27/projects/index.php/index/user") 
# print(response.cookies) 
# PHP = response.cookies.get("PHPSESSID") 
# print(PHP)

# response = requests.post(
#     "http://39.105.34.27/projects/index.php/index/user/login.html",
#     data={"mobile":"admin","password":"admin","type":"1"},
#     cookies={"PHPSESSID":"PHP"},
#     headers={"X-Requested-With": "XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded"})
# print(response.text)
# aa=response.headers
# ck=aa["Set-Cookie"]
# print(ck.split(";"))
# ck1=ck.split(";")[0]
# print(ck1)

# response = requests.post(
#     "http://39.105.34.27/projects/index.php/index/address/add.html",
#     json={
#         "username":"fewf",
#         "province":"浙江省",
#         "city":"杭州市",
#         "area":"西湖区",
#         "address":"fdsfsdf",
#         "mobile":"dfsf",
#         "id":"123"},
#     cookies={"PHPSESSID":"PHP"},
# headers={
#     "X-Requested-With": "XMLHttpRequest",
#     "Content-Type":"application/x-www-form-urlencoded"})
# print(response.text)


# 练习
import requests

# response = requests.post("http://aabad.cn:3001/api/student/user/register",
# json={
#     "userName":"student10",
#     "password":"123456",
#     "userLevel":1},
# )
# print(response.text)


# session = requests.session()
# response = session.post("http://aabad.cn:3001/api/user/login",
# json={"userName":"student",
# "password":"123456",
# "remember":False,   
# })
# result = response.json()

'''
不用session会话的时候用requests.post方法
# response = requests.post("http://aabad.cn:3001/api/user/logout",
# cookies=response.cookies,
# )
# print(response.text)


# response = requests.post("http://aabad.cn:3001/api/student/dashboard/index",
# cookies=response.cookies
# )
# print(response.json())


# response = requests.post("http://aabad.cn:3001/api/student/dashboard/task",
# cookies=response.cookies
# )
# print(response.json())
'''


# 使用session会话的时候使用session.post方法，在登录前建立会话
# response = session.post("http://aabad.cn:3001/api/user/logout",
# )
# print(response.text)
