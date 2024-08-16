import requests
import sys

import requests.auth

#if len(sys.argv) != 4:
#    print("Usage: list-camera-parameters.py <ip> <username> <password>")
#    sys.exit(1)

ip = '192.168.1.66'#sys.argv[1]
username = "viewer"#sys.argv[2]
password = "view"#sys.argv[3]

auth = requests.auth.HTTPDigestAuth(username, password)

#auth = requests.auth.HTTPBasicAuth(username, password)
r = requests.get("http://{}/axis-cgi/admin/param.cgi?action=list&group".format(ip), auth=auth)



print(r.status_code)
print(r.text)

r = requests.get("http://{}/axis-cgi/param.cgi?action=list&group=Brand".format(ip), auth=auth)

print(r.status_code)
print(r.text)