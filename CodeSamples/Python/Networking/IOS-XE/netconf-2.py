from ncclient import manager
# import logging
# logging.basicConfig(level=logging.DEBUG)

router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
          "username": "developer", "password": "C1sco12345"}

m = manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False)

for capability in m.server_capabilities:
    print('*','--' * 50,'*')
    print(capability)

m.close_session()
