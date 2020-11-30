
from requests.auth import HTTPBasicAuth
import requests

auth = HTTPBasicAuth('cisco', 'cisco')
url = 'http://csr1kv/restconf/api/config/native/interface'
response = requests.get(url, verify=False, auth=auth)

headers = { 'Accept': 'application/vnd.yang.data+json' }
response = requests.get(url, verify=False, headers=headers, auth=auth)

response = requests.get(url+'?deep', verify=False, headers=headers, auth=auth)
