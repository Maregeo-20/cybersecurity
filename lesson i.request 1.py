import requests

payload={'firstName':'Rocco','lastName':'Siffredi'}
r=requests.get('https://httpbin.org/get', params = payload)
print(r.text)