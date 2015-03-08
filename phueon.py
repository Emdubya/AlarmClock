#! /usr/bin/python

from phue import Bridge

b = Bridge('192.168.1.120')

b.connect()

b.get_api()

#b.set_light([1,2,3], 'on', False)

tran = {'transitiontime' : 300, 'on' : True, 'bri' : 254, 'hue' : 34495}

b.set_light([1,2,3], tran)
