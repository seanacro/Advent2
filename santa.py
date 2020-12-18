#!/usr/bin/python3

import requests

ip = input(str("Enter assigned machine IP \n"))
key = 1
print('\n')
session = requests.Session()

while int(key) < 100:
    url = "http://%s:8000/api/%s" % (ip, str(key))
    r = session.get(url)
    output = r.json()
    print(str(output['item_id'] + '\t' + output['q'])
    key += 2
    if 'Error' not in output['q']:
        break
