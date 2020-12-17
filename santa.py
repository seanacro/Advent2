#!/usr/bin/python3

import requests

ip = input(str("Enter assigned machine IP \n"))
key = 1
print('\n')
session = requests.Session()

while int(key) < 100:
    url = "http://%s:8000/api/%s" % (ip, str(key))
    r = session.get(url)
    content = r.text
    print(str(key) + '\t' + url)
    key += 2
    if "Error" in content:
        pass
    elif "PROTECTION" in content:
        print(content)
        break
    else:
        print(content)
        break
