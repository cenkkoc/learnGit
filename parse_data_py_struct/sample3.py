import xmltodict

#Get the XML file data
stream = open('C:/Users/Cenk/Dropbox/GitHub/learnGit/parse_data_py_struct/sample.xml','r')

#Prase the XML file into an 'OrderedDict'
xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    print(e)

