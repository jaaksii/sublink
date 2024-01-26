import requests
import json
class Xui():
    def __init__(self):
        self.cookie = {}
        self.url = ''
    def Login(self,username,password):
        url = f'{self.url}/login'
        data = {
            'username': username,
            'password': password
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        response = requests.post(url=url, data=data, headers=headers)
        response_data = json.loads(response.text)
        msg = response_data.get('msg')
        if response.status_code == 200 and msg == '登录成功':
            self.cookie = response.cookies.get('session')
            if self.cookie != '':
                return True
        else:
            print(f'''
            错误信息:{msg}
                  ''')
            return False
    def List(self):
        url = f'{self.url}/xui/inbound/list'
        headers = {
            'Cookie':f'session={self.cookie}'
        }
        response = requests.post(url=url,headers=headers)
        if response.status_code == 200:
            # text = json.loads(response_data.text)
            response_data = json.loads(response.text, strict=False)
            objs = response_data['obj']
            # print(response_data)
            for obj in objs:
                settings = json.loads(obj['settings'])
                clients = settings.get('clients')
                data = {
                    'remark': obj['remark'],
                    'up': obj['up'],
                    'down': obj['down'],
                    'total': obj['total'],
                    'protocol': obj['protocol'],
                }
                print(data)
xui = Xui()
xui.url = 'http://127.0.0.1:12345'
login = xui.Login('admin','admin')
if login:
    xui.List()
