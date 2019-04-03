import requests
from configparser import ConfigParser

class Config:
    def __init__(self):
     parser = ConfigParser()
     parser.read('database.config')

    def Headers(self,parser):
        headers = parser.get('database_config', 'headers')

        return headers
   # print(Headers())
    def credentials(self,parser):

        login_data = parser.get('database_config', 'login_data')
        print(login_data)
        # login_data = {
        #     'userName': 'Amey.Patil@quest-global.com',
        #     'password': 'Quest=1234',
        #     'Login': 'Log in'
        # }
        #return login_data
    # print(credentials())

    def session(self,parser):
        session = parser.get('database_config', 's')
        return session

    '''def session(self,headers,credentials):
        with requests.session() as s:
            url = "https://rolls-royce.leankit.com/Account/Membership/Authenticate?support=False"
            r1 = s.get(url, headers=headers)
            r2 = s.post(url, data=credentials, headers=headers)
            r3 = s.get("https://rolls-royce.leankit.com/io/user/me/board/recent?_=1551685125246")
        return url,r1,r2,r3
    #print(session(Headers(), credentials()))'''






















