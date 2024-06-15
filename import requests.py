import requests

headers = {'user-agent': 'my-app/0.0.1'}
payload = {'message_id': '1','like':'like'}
jar = requests.cookies.RequestsCookieJar()
jar.set('eyJ1c2VyIjoiYSJ9', 'ZmsBLw.kyhM9hloYfkTbSAa2CWiFuVqClA')

#r = requests.get('http://httpbin.org/get', params=parameters, headers=headers)
r = requests.post('https://thelikebutton.techcamp.towerofhanoi.it/post', headers=headers, data=payload, cookies=jar)

print(r.text)
print(r.status_code)