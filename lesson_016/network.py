import urllib.request
import requests

# password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = 'https://httpbin.org/basic-auth/user/passwd'
# password_mgr.add_password(None, top_level_url, 'user', 'passwd')
# handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
# opener = urllib.request.build_opener(handler)
# response = opener.open(top_level_url)
# print(f'Код состояния {response.getcode()}')
# print(f'Тело ответа {response.read()}')

response = requests.get(top_level_url, auth=('user', 'passwd'))
# print(f'Код состояния {response.status_code}')
# print(f'Тело ответа в байтах {response.content}')
# print(f'Тело ответа в str {response.text}')
# print(f'Тело ответа в json {response.json()}')
# print(f'Ответ с заголовками {response.request.headers}')

url_get = 'https://httpbin.org/get'
headers = {'Skillbox': '16 module',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
           }
response_with_headers = requests.get(url_get, headers=headers)
# print(f'Ответ сервера, включающий и переданные нами заголовки, {response_with_headers.text}')

url_post = 'https://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
response_with_data = requests.post(url_post, data=payload, headers=headers)
# print(f'Ответ сервера, включающий данные и заголовки, {response_with_data.text}')
response_with_redirect = requests.get('https://gitlab.skillbox.ru/learning_materials/python_base')
# print(f'В результате мы оказались на {response_with_redirect.url}')
# print(f'Итоговый код состояния {response_with_redirect.status_code} {response_with_redirect}')
# print(f'Итоговый код состояния {response_with_redirect.text}')
# print(f'История редиректов {response_with_redirect.history}')

# try:
#     response_with_timeout = requests.get('https://gitlab.skillbox.ru', timeout=0.01)
# except requests.exceptions.ReadTimeout:
#     print('HTTPSConnectionPool(host="gitlab.skillbox.ru", port=443): Read timeout. (read timeout=0.01)')


class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        # implement my authentication
        r.headers['MyAuth'] = '123'
        return r


print(requests.get(url_get, auth=MyAuth()).text)
