import requests
import json

from pprint import pprint

url = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

payload = {}
headers = {
  'Acc': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data = payload, verify=False)

api_data = response.json()

print ("*" * 50)
pprint (["Cisco-IOS-XE-interfaces-oper:interfaces"]["description"])
print ("*" * 50)

