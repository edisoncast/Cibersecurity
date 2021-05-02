#!/usr/bin/python3

#Extraccion de la clave con xor

import base64, json

#Se obtiene del parámetro set cookie data=ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D, el %3D es un igual

ciphertext = b"ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="

# Base 64 decode

ciphertext = base64.decodebytes(ciphertext)

plaintext = {"showpassword":"no", "bgcolor":"#ffffff"}
plaintext = json.dumps(plaintext).encode('UTF-8').replace(b" ", b"")

def xor_decrypt(ciphertext, plaintext):
    key = ""

    for x in range(len(ciphertext)):
        key += str(chr(ciphertext[x] ^ plaintext[x % len(plaintext)]))
    
    return key

def xor_encrypt(ciphertext, plaintext):
    secret = ""

    for x in range(len(ciphertext)):
        secret += str(chr(ciphertext[x] ^ plaintext[x % len(plaintext)]))
    
    secret = base64.encodebytes(secret.encode('utf-8'))
    return secret

key = xor_decrypt(ciphertext, plaintext)
print(key)

key2 = b"qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw"

new_cookie = {"showpassword":"yes", "bgcolor":"#ffffff"}
new_cookie = json.dumps(new_cookie).encode('UTF-8').replace(b" ", b"")

flag = xor_encrypt(key2, new_cookie)

print(flag)




