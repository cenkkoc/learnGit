import requests
from pprint import pprint


##### LOgin

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\":{\n\t\t\"attributes\":{\n\t\t\"name\":\"admin\",\n\t\t\"pwd\":\"Admin_1234!\"\n\t\t}\n\t\t\n\t}\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
  'Content-Type': 'text/plain',
  'Cookie': 'APIC-cookie=JJ4hE/XqV6KI3g1LOUAYUe/AeMjfSmSKZfRqKPlXoYXN2yenxuN7bS/T7gZhlqCCP7x66Ntiv2VESItsOcdrbJuXv5sd8QsU/eaHPkysJu18V3hzDqy7lWLP8mY4K3hADSHnW2AoGN2Rxdr9ADbrrKapp+w/dXEHlddacc7lSMk='
}

response = requests.request("POST", url, headers=headers, data = payload, verify=False).json()

#pprint(response)

token = response['imdata'][0]['aaaLogin']['attributes']['token']

#print (token)

cookies={}
cookies['APIC-cookie']=token


#### UPDATE eth desc



url = "https://sbx-nxos-mgmt.cisco.com:443/api/node/mo/sys/intf/phys-[eth1/33].json"

payload = "{\n\t\"l1PhysIf\":{\n\t\t\"attributes\":{\n\t\t\t\"descr\":\"Python Demo\"\n\t\t}\n\t}\n}"
headers = {
  
  'Content-Type': 'text/plain',
  
}

put_response = requests.request("PUT", url, headers=headers, data = payload, verify=False, cookies=cookies).json()

pprint(put_response)




