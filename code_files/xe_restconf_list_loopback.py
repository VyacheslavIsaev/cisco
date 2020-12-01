import requests
from requests.auth import HTTPBasicAuth

#
# Disabling insecure request warning
#
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#
# Note: It's a bad practice to keep username and password inside code file.
#
auth = HTTPBasicAuth('cisco', 'cisco')

url = "https://csr1kv/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback?fields=name"

headers = {
    'Accept': 'application/yang-data+json'
    }

response = requests.request("GET", url, headers=headers, verify=False, auth=auth)

print(response.text)