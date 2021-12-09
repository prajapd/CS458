import nacl.utils 
from nacl.public import PrivateKey 
from nacl.encoding import HexEncoder 
import nacl.secret
import requests 
import json 
import base64 
from nacl.signing import SigningKey

#note: remember to use key.decode(encoder=HexEncoder) to return to byte 
	#the keys are in byte form already
signing_key = SigningKey.generate()
verify_key = signing_key.verify_key


base64_string = base64.b64encode(verify_key.encode()).decode("ascii")
	
url = "https://hash-browns.cs.uwaterloo.ca/api/signed/set-key"

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"public_key": base64_string
}

headers = {
"content-type": "application/json", 
"accept": "application/json"
}
	
response = requests.post(url, data=json.dumps(params), headers=headers) 

print(response.text)
print(response.status_code, response.reason)
	
url = "https://hash-browns.cs.uwaterloo.ca/api/signed/send"


signed = signing_key.sign(b"hello again, Scholar")

encrypted_bytes = base64.b64encode(signed)
encrypted_string = encrypted_bytes.decode("ascii")

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"to": "Scholar",
"message": encrypted_string 
}

response = requests.post(url, data=json.dumps(params), headers=headers)
print(response.text)
print(response.status_code, response.reason)

 
