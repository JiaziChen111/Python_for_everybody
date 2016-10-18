# -*- coding: utf-8 -*-
"""
Created on  3:02 2016/10/5

author  songxf
"""
# Assignment 1

import urllib.request
# import xml.etree.ElementTree as ET
import json

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	print('Retrieving', address)
	uh = urllib.request.urlopen(address)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')
	# print(data)
	info = json.loads(data)
	print('User count:', len(info["comments"]))
	a = 0
	for item in info["comments"]:
		a = a + item['count']
	print(a)
		# print('Name', item['name'].encode())
		# print('Id', item['id'].encode())
		# print('Attribute', item['x'].encode())


# Assignment 2

import urllib.request
import urllib.parse
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = input('Enter location: ')
	if len(address) < 1 : break

	url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
	print('Retrieving', url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')

	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print('==== Failure To Retrieve ====')
		print(data)
		continue

	#print(json.dumps(js, indent=4))
	plcid=js['results'][0]['place_id']
	print(plcid)
	#lat = js["results"][0]["geometry"]["location"]["lat"]
	#lng = js["results"][0]["geometry"]["location"]["lng"]
	#print('lat', lat, 'lng', lng)
	#location = js['results'][0]['formatted_address']
	#print(location)













