#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import time
import textwrap
from better_spoken_time3 import gmt, day
#from get_url_btc4 import btc
from get_url_weather9 import wtr, frc
from get_url_news8 import canadanews, technews
from time import sleep

count = 1


# your name goes here:
name = 'Matt.'

# key to getting text to speech
head = 'wget -q -U Mozilla '
tail = '.mp3 '

# end
end = 'Thats all for now. Now wake your ass up and Have a nice day.  '

# Turn all of the parts into a single string
wad = (gmt + name + day + wtr + frc + canadanews + technews + end)
# print wad

# strip any quotation marks
wad = wad.replace('"', '').strip()
wad = wad.replace("'", '').strip()

# If you want to say with pure FOSS projects, use festival instead of google tts by uncommenting out the line below AND commenting out EVERYTHING else
# print subprocess.check_output("echo " + wad + " | festival --tts ", shell=True)

# Google voice only accepts 100 characters or less, so split into chunks
shorts = []
for chunk in wad.split('.  '):
    shorts.extend(textwrap.wrap(chunk, 100))


# Send shorts to Google and return mp3s
try:
  for sentence in shorts:
    sendthis = sentence.join(['"http://translate.google.com/translate_tts?tl=en&q=', '" -O /mnt/ram/'])
    print(head + sendthis + str(count).zfill(2) + str(tail))
    print subprocess.check_output (head + sendthis + str(count).zfill(2) + str(tail), shell=True)
    count = count + 1

  print subprocess.call ('/home/pi/phueon.py', shell=True) #turn on the lights
# Play the mp3s returned
  print subprocess.call ('/usr/bin/mpg123 -h 10 -d 11 /mnt/ram/*.mp3', shell=True)

# festival is now called in case of error reaching Google
except subprocess.CalledProcessError:
  print subprocess.check_output("echo " + wad + " | festival --tts ", shell=True)

# Cleanup any mp3 files created in this directory.
print 'cleaning up now'
print subprocess.call ('rm /mnt/ram/*.mp3', shell=True)
print subprocess.call ('/usr/bin/omxplayer /home/pi/share/*.mp3', shell=True)
time.sleep(7200) #delay for 2 hours
print subprocess.call ('/home/pi/phueoff.py', shell=True) #shut off the lights
