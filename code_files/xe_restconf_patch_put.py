
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
xml_headers = {'Content-Type': 'application/yang-data+xml'}

loopback_interface_data_min = """<Loopback><name>1</name></Loopback>"""

loopback_interface_data_primary_address = """<Loopback><name>1</name><ip><address><primary><address>10.101.1.2
</address><mask>255.255.255.0</mask></primary></address></ip></Loopback>"""

loopback_interface_data_secondary_address = """
<Loopback><name>1</name>
    <ip><address><secondary>
        <address>10.101.1.3</address>
        <mask>255.255.255.0</mask>
        <secondary/>
    </secondary></address></ip>
</Loopback>"""

response = requests.request("DELETE", url+'/Loopback=1', verify=False, auth=auth)

response = requests.request("PUT", 
                        url+"/Loopback=1", 
                        data=loopback_interface_data_min,
                        headers=xml_headers, 
                        verify=False, 
                        auth=auth)
print("Creating interface. PUT status code: "+str(response.status_code))

response = requests.request("PATCH", 
                        url+"/Loopback", 
                        data=loopback_interface_data_primary_address,
                        headers=xml_headers, 
                        verify=False, 
                        auth=auth)
print("Configuring primary address. PATCH status code: "+str(response.status_code))

response = requests.request("PUT", url+"/Loopback=1", 
                        data=loopback_interface_data_secondary_address, 
                        headers=xml_headers, 
                        verify=False, 
                        auth=auth)
print("Configuring secondary address. PUT status code: "+str(response.status_code))

response = requests.request("PATCH",
                        url+"/Loopback=1", 
                        data=loopback_interface_data_secondary_address, 
                        headers=xml_headers, 
                        verify=False, 
                        auth=auth)
print("Configuring secondary address. PATCH status code: "+str(response.status_code))

response = requests.request("GET",
                        url+"/Loopback=1", 
                        headers=xml_headers, 
                        verify=False, 
                        auth=auth)
print("Interface configuration: \n"+response.text)
