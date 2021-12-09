import requests 
import json 
import nacl.utils
import nacl.secret 
import base64
from binascii import unhexlify 

url = "https://hash-browns.cs.uwaterloo.ca/api/psk/send"

key = bytes.fromhex("f2a974200dcffb0ba53743599aead979837010d350c7c5e7d54e286c1e658961")

box = nacl.secret.SecretBox(key)

message = b"hello Scholar"

encrypted_bytes = base64.b64encode(box.encrypt(message)) 
encrypted_string = encrypted_bytes.decode("ascii")

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"to": "Scholar",
"message": encrypted_string 
}

headers = {
"content-type": "application/json",
"accept": "application/json"
}

response = requests.post(url, data=json.dumps(params), headers=headers)

print(response.text)
print(response.status_code, response.reason)

url = "https://hash-browns.cs.uwaterloo.ca/api/psk/inbox"

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1"
}

response = requests.post(url, json.dumps(params), headers=headers)

print(box.decrypt(base64.b64decode(json.loads(response.text)[0]['message'])))
print(response.status_code, response.reason)
