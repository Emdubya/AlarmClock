#! /usr/bin/python

from phue import Bridge

b = Bridge('192.168.1.120')

b.connect()

b.get_api()

tran = {'transitiontime' : 300, 'on' : False}

b.set_light([1,2,3], tran)
