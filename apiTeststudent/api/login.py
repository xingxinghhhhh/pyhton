import requests


class login_api:
    session = requests.session()
    def __init__(self):
        self.login_url = "http://aabad.cn:3001/api/user/login"
        self.shouye_url = "http://aabad.cn:3001/api/student/dashboard/index"

# 登录的接口
    def login_user(self,userName,password,remember):
        data={"userName":userName,"password":password,"remember":remember,}
        
        return login_api.session.post(self.login_url,json=data)

# 获取首页的接口，保持会话
    def shouye(self):
        a=login_api.session.request("post",self.shouye_url)
        return a
