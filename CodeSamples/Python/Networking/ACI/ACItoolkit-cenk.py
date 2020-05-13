from acitoolkit.acitoolkit import *


url = 'https://sandboxapicdc.cisco.com'
user = 'cisco'
pw = 'ciscopsdt'


session = Session(url,user,pw)

session.login()