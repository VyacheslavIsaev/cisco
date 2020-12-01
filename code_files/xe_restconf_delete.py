from requests.auth import HTTPBasicAuth
import requests

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#
# Note: It's a bad practice to keep username and password inside code file.
#
auth = HTTPBasicAuth('cisco', 'cisco')
url = 'https://csr1kv/restconf/data/Cisco-IOS-XE-native:native/interface'
xml_headers = {'Content-Type': 'application/vnd.yang.data+json'}

response = requests.request("DELETE", url+'/Loopback=1', verify=False, auth=auth)
print(response.text)
print("Deleting Loopback interface with the name 1:")
if (response.status_code==204):
    print ("Succeed")
else:
    print ("Failed")
print("With status code: "+str(response.status_code))