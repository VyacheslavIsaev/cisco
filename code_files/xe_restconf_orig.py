from requests.auth import HTTPBasicAuth
import requests

#
# Note: It's a bad practice to keep username and password inside code file.
#
auth = HTTPBasicAuth('cisco', 'cisco')
url = 'http://csr1kv/restconf/api/config/native/interface'
xml_headers = {'Content-Type': 'application/vnd.yang.data+xml'}

gigabit_interface_data  = """<GigabitEthernet><name>1</name></GigabitEthernet>"""
loopback_interface_data = """<Loopback><name>1</name></Loopback>"""

response = requests.post(url, data=gigabit_interface_data, headers=xml_headers, verify=False, auth=auth)

response = requests.post(url, data=loopback_interface_data, headers=xml_headers, verify=False, auth=auth)

response = requests.delete(url+'/Loopback=1', verify=False, auth=auth)
