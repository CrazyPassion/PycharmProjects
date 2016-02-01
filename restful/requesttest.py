#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# r = requests.get('http://127.0.0.1:5000/login', auth=('magigo', '123456'))
# print r.text

r = requests.get('https://github.com', auth=('CrazyPassion', '357951jey'))
print r.text


# token ='bWFnaWdvOjAuMDEyMjY2MDYxMzc5NToxNDQyODU2MjYxLjk2'
# r = requests.get('http://127.0.0.1:5000/test1', params={'token': token})
# print r.text

# bWFnaWdvOjAuMzE4MTUxNTA1MjQ4OjE0MjU4MzkzMjMuODk=