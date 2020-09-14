import requests
import json

url='https://devnetapi.cisco.com/sandbox/apic_em/api/v1/ticket'
payload = {"username":"devnetuser","password":"Cisco123!"}

header = {"content-type": "application/json"}
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
print(response.text)
