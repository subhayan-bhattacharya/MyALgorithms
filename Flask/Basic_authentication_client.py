import requests
from requests.auth import HTTPBasicAuth
import os
import sys

proxies = {
  'http': 'http://www-proxy.us.oracle.com:80',
  'https': 'http://www-proxy.us.oracle.com:80',
}

#Deleting proxies
for k in list(os.environ.keys()):
    if k.lower().endswith('_proxy'):
        del os.environ[k]

payload = {"name":"Subhayan","lastname": "Bhattacharya"}
r = requests.post('https://127.0.0.1:5000/test',data=payload,auth=HTTPBasicAuth('Subhayan','Bhattacharya'))
print r
if r.status_code != 200:
    print r.status_code
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print "Exception caught with HTTPError"
    except requests.exceptions.ConnectionError as e:
        print "There is a connection error"
    except:
        print "Does it come here ??"
        print e
    
else:
    response = r.json()
    for key in response:
        print key,response[key]





