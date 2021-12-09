import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
from nacl.encoding import Base64Encoder, HexEncoder, RawEncoder
import nacl.secret
import requests
import json
import base64
from nacl.signing import SigningKey, VerifyKey

url = "https://hash-browns.cs.uwaterloo.ca/api/prekey/set-identity-key"

signing_key = SigningKey.generate()
verify_key = signing_key.verify_key

ver_key_encoded = base64.b64encode(verify_key.encode()).decode("ascii")

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"public_key": ver_key_encoded
}

headers = {
"content-type": "application/json",
"accept": "application/json"
}

response = requests.post(url, data=json.dumps(params), headers=headers)

print(response.text)
print(response.status_code, response.reason)

url = "https://hash-browns.cs.uwaterloo.ca/api/prekey/set-signed-prekey"

sk_disa = PrivateKey.generate()
pk_disa = sk_disa.public_key
pk_disa_encoded = pk_disa.encode(encoder=RawEncoder)

signed = signing_key.sign(pk_disa_encoded)

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"public_key": base64.b64encode(signed).decode("ascii")
}

response = requests.post(url, data=json.dumps(params), headers=headers)

print(response.text)
print(response.status_code, response.reason)

url = "https://hash-browns.cs.uwaterloo.ca/api/prekey/get-identity-key"

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"user": "Scholar"
}

response = requests.post(url, data=json.dumps(params), headers=headers)

#base64 key
verification_key_scholar = json.loads(response.text)['public_key']

#decoded - verify_key
verification_key_decoded_scholar = base64.b64decode(verification_key_scholar)

print(response.text)
url = "https://hash-browns.cs.uwaterloo.ca/api/prekey/get-signed-prekey"

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"user": "Scholar"
}

response = requests.post(url, data=json.dumps(params), headers=headers)

key_signed_scholar = json.loads(response.text)['public_key']
decoded_signed_scholar = base64.b64decode(key_signed_scholar)

verification_scholar = VerifyKey(verification_key_decoded_scholar)
key_scholar = verification_scholar.verify(decoded_signed_scholar)
pk_scholar = PublicKey(key_scholar)

message = b"GoodBye ... Scholar"

box_disa = Box(sk_disa, pk_scholar)
encrypted = box_disa.encrypt(message, encoder=Base64Encoder).decode("ascii") 

url = "https://hash-browns.cs.uwaterloo.ca/api/prekey/send" 

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1","to": "Scholar",
"message": encrypted
}

response = requests.post(url, data=json.dumps(params), headers=headers)

print(response.text)
print(response.status_code, response.reason) 

url = "https://hash-browns.cs.uwaterloo.ca/api/prekey/inbox"

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1"
}

response = requests.post(url, data=json.dumps(params), headers=headers)

scholar_response_decoded = base64.b64decode(json.loads(response.text)[0]['message'])

print(box_disa.decrypt(scholar_response_decoded))
