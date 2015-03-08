#!/usr/bin/env python

import feedparser

try:
#    rss = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
    canadarss = feedparser.parse('http://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009')
    techrss = feedparser.parse('http://www.ctvnews.ca/rss/ctvnews-ca-sci-tech-public-rss-1.822295')

#for entry in rss.entries[:4]:
#    print entry['title']
#    print entry['description']
#
#print rss.entries[0]['title']
#print rss.entries[0]['description']
#print rss.entries[1]['title']
#print rss.entries[1]['description']
#print rss.entries[2]['title']
#print rss.entries[2]['description']
#print rss.entries[3]['title']
#print rss.entries[3]['description']

    canadanewsfeed = canadarss.entries[0]['title'] + '.  ' + canadarss.entries[0]['description'] + '.  ' + canadarss.entries[1]['title'] + '.  ' + canadarss.entries[1]['description'] + '.  ' + canadarss.entries[2]['title'] + '.  ' + canadarss.entries[2]['description'] + '.  ' + canadarss.entries[3]['title'] + '.  ' + canadarss.entries[3]['description'] + '.  '
    technewsfeed = techrss.entries[0]['title'] + '.  ' + techrss.entries[0]['description'] + '.  ' + techrss.entries[1]['title'] + '.  ' + techrss.entries[1]['description'] + '.  ' + techrss.entries[2]['title'] + '.  ' + techrss.entries[2]['description'] + '.  ' + techrss.entries[3]['title'] + '.  ' + techrss.entries[3]['description'] + '.  '

# print newsfeed

# Today's news from BBC
    canadanews = 'Now, The latest stories from the Canada section of the CTV News RSS feed.  ' + canadanewsfeed
    technews = 'And now, The latest stories from the technology section of the CTV News RSS feed.  ' + technewsfeed

except canadarss.bozo:
    canadanews = 'Failed to reach CTV News'

except techrss.bozo:
    technews = 'Failed to reach CTV News'

# print news
