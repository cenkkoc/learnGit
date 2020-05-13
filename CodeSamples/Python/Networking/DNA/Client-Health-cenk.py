import requests
import json
#from pprint import pprint


################ LOGIN ######################
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
pw = 'Cisco123!'

response = requests.post(url, auth=(user, pw)).json()
#print(response)
token = response['Token']

############### client health

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"
query_string = {"timestamp": "1589397245173"}

headers = {
    'x-auth-token':token
}

response = requests.get(url, headers=headers, params=query_string).json()

#print (json.dumps(response, indent=2, sort_keys=True))

print(f"clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")