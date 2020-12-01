
from requests.auth import HTTPBasicAuth
import requests

auth = HTTPBasicAuth('cisco', 'cisco')
url = 'https://csr1kv/restconf/data/Cisco-IOS-XE-native:native/interface'
xml_headers = {'Content-Type': 'application/vnd.yang.data+xml'}

loopback_interface_data_min = """ <Loopback><name>1</name></Loopback>"""
loopback_interface_data_primary_address = """<Loopback><name>1</name><ip><address><primary><address>10.101.1.2
</address><mask>255.255.255.0</mask></primary></address></ip></Loopback>"""

loopback_interface_data_secondary_address = """<Loopback><name>1</name><ip><address><secondary><address>10.101.1.3
</address><mask>255.255.255.0</mask></secondary></address></ip></Loopback>"""

response = requests.put(url+"/Loopback/1", data=loopback_interface_data_min,
headers=xml_headers, verify=False, auth=auth)

response = requests.patch(url+"/Loopback", data=loopback_interface_data_primary_address,
headers=xml_headers, verify=False, auth=auth)

response = requests.put(url+"/Loopback/1", data=loopback_interface_data_secondary_address, headers=xml_headers, verify=False, auth=auth)


response = requests.patch(url+"/Loopback", data=loopback_interface_data_secondary_address, headers=xml_headers, verify=False, auth=auth)
