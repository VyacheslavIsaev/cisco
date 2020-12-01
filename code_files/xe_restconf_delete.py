from requests.auth import HTTPBasicAuth
import requests

#
# Note: It's a bad practice to keep username and password inside code file.
#
auth = HTTPBasicAuth('cisco', 'cisco')
url = 'https://csr1kv/restconf/data/Cisco-IOS-XE-native:native/interface'
xml_headers = {'Content-Type': 'application/vnd.yang.data+xml'}

response = requests.request("DELETE", url+'/Loopback=1', verify=False, auth=auth)
print(response.text)
