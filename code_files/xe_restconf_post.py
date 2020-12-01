from requests.auth import HTTPBasicAuth
import requests

#
# Disabling insecure request warning
#
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#
# Note: It's a bad practice to keep username and password inside code file.
#
auth = HTTPBasicAuth('cisco', 'cisco')
url = 'https://csr1kv/restconf/data/Cisco-IOS-XE-native:native/interface'
xml_headers = { }

gigabit_interface_data  = """<GigabitEthernet><name>1</name></GigabitEthernet>"""
loopback_interface_data = """<Loopback><name>1</name></Loopback>"""

response = requests.request("POST", url, data=gigabit_interface_data, headers=xml_headers, verify=False, auth=auth)
print (response.text)
print ("Adding GigabitEthernet with name 1:")
if (response.reason==200):
    print ("Succeed")
else:
    print ("Failed")

response = requests.request("POST", url, data=loopback_interface_data, headers=xml_headers, verify=False, auth=auth)
print (response.text)
print ("Adding Loopback interface with the name 1:")
if (response.reason==200):
    print ("Succeed")
else:
    print ("Failed")





