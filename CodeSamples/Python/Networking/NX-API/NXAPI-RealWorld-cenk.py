import requests
import json
from pprint import pprint

switch_user = 'admin'
switch_password = 'Admin_1234!'


url='https://sbx-nxos-mgmt.cisco.com/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show int br",
    "output_format": "json"
  }
}

response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switch_user,switch_password), verify=False).json()

#pprint(response)

#### Login with NX-API Rest

auth_url = 'https://sbx-nxos-mgmt.cisco.com/api/mo/aaaLogin.json'
auth_body = {
    "aaaUser": {
        "attributes": {
            "name":switch_user, 
            "pwd":switch_password
            }
            }
            }

auth_response = requests.post(auth_url, data=json.dumps(auth_body), timeout=5, verify=False).json()

token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token

#print(cookies)
            

counter = 0
int_response = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
int_counter = len(int_response)

"""
{'interface': 'Ethernet1/4', 'vlan': '1', 'type': 'eth', 'portmode': 'access', 'state': 'up', 'state_rsn_desc': 'none', 'speed': '1000', 'ratemode': 'D'}
"""

# print (int_counter)

while counter < int_counter-20:
    
    print ("*"*30)
    # buraya regex if yazılmalı
    print (int_response[counter]['interface']," + ",int_response[counter]['state'])
    counter += 1
print ("*"*30)

#print (int_response)


