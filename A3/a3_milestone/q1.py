import requests 
import json


url = "https://hash-browns.cs.uwaterloo.ca/api/plain/send"

params = {
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1",
"to": "Scholar", 
"message": "SGVsbG8sIFdvcmxkIQ==" 
}

headers = {
"content-type": "application/json",
"accept": "application/json"
}

response = requests.post(url, data=json.dumps(params), headers=headers)

print(response.text)
print(response.status_code, response.reason) 

url = "https://hash-browns.cs.uwaterloo.ca/api/plain/inbox"

params = { 
"api_token": "a4f5c25935b8d286903c3897e64ea16d5430e10dac6678bb543fd6b873a8deb1" 
}

response = requests.post(url, json.dumps(params), headers=headers)

print(response.json())  
