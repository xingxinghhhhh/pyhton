import requests


class aaa:
    def __init__(self):
        self.login_url = "http://aabad.cn:3001/api/user/login"

    def bbb(self,userName,password,remember):
        data={"userName":userName,"password":password,"remember":remember,}
        
        return requests.post(self.login_url,json=data)