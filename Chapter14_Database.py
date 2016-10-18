# -*- coding: utf-8 -*-
"""
Created on  11:39 2016/10/3

author  songxf
"""

import json

data = '''{
"name" : "Chuck",
"phone" : {
"type" : "intl",
"number" : "+1 734 303 4456"
},
"email" : {
"hide" : "yes"
}
}'''
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

import json

data = '''[
{ "id" : "001",
"x" : "2",
"name" : "Chuck"
} ,
{ "id" : "009",
"x" : "7",
"name" : "Chuck"
}
]'''  # 是一个列表，其中的元素是dictionary
info = json.loads(data)
print('User count:', len(info))
for item in info:
	print('Name', item['name'])
	print('Id', item['id'])
	print('Attribute', item['x'])

# Accessing APIS in Python

import urllib.parse
import urllib.request
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	url = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address})
	print('Retrieving', url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')
	try:
		js = json.loads(str(data))
	except:
		js = None
	if 'status' not in js or js['status'] != 'OK':
		print('==== Failure To Retrieve ====')
		print(data)
		continue
	print(json.dumps(js, indent=4))
	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lng"]
	print('lat', lat, 'lng', lng)
	location = js['results'][0]['formatted_address']
	print(location)

import twurl
import json
import urllib.request

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
while True:
	print('')
	acct = input('Enter Twitter Account:')
	if (len(acct) < 1): break
	url = twurl.augment(TWITTER_URL,
						{'screen_name': acct, 'count': '5'})
	print('Retrieving', url)
	connection = urllib.request.urlopen(url)
	data = connection.read().decode()
	headers = connection.info().dict
	print('Remaining', headers['x-rate-limit-remaining'])
	js = json.loads(data)
	print(json.dumps(js, indent=4))
	for u in js['users']:
		print(u['screen_name'])
		s = u['status']['text']
