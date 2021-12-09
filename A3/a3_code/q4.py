import nacl.utils 
from nacl.public import PrivateKey, PublicKey, Box
from nacl.encoding import Base64Encoder, HexEncoder
from nacl.hash import blake2b 
import requests 
import json 
import base64

url = "https://hash-browns.cs.uwaterloo.ca/api/pke/get-key"

params = {
	"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
	"user" : "Scholar"
} 

headers = {
	"content-type": "application/json",
	"accept": "application/json"
}

response = requests.post(url, data=json.dumps(params), headers=headers)

print(response.text)
print(response.status_code, response.reason)

#base64 key that is of type string 
key_scholar = json.loads(response.text)['public_key']

#decoded in bytes
pk_scholar = base64.b64decode(key_scholar)

hash_scholar = blake2b(pk_scholar)

print("hash: ")
print(hash_scholar)


url = "https://hash-browns.cs.uwaterloo.ca/api/pke/set-key" 


sk_disa = PrivateKey.generate()
pk_disa = sk_disa.public_key

base64_string = pk_disa.encode(encoder=Base64Encoder).decode("ascii")

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1","public_key": base64_string
}


response = requests.post(url, data=json.dumps(params), headers=headers)

print(response.text)
print(response.status_code, response.reason)


url = "https://hash-browns.cs.uwaterloo.ca/api/pke/send"

box_disa = Box(sk_disa, PublicKey(pk_scholar)) 

message = b"hello, Scholar"

encrypted = box_disa.encrypt(message, encoder=Base64Encoder)

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"to": "Scholar",
"message": encrypted.decode("ascii")
}

response = requests.post(url, data=json.dumps(params), headers=headers)

print(response.text)
print(response.status_code, response.reason)

url = "https://hash-browns.cs.uwaterloo.ca/api/pke/inbox"

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1"
}

response = requests.post(url, data=json.dumps(params), headers=headers)

scholar_response_decoded = base64.b64decode(json.loads(response.text)[0]['message'])


print(box_disa.decrypt(scholar_response_decoded))
