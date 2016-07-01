#!usr/bin/env python

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from BeautifulSoup import BeautifulSoup as bs
import urllib2, webbrowser, re, time

names = []
timings = []

fifteen_minutes = '00:15:00'
link = 'https://codeforces.com'
f = urllib2.urlopen(link).read()
soup = bs(f)


search = re.compile('/contests/*')
l = []
s = '[0-9]'
t = ''
l.append(s)
for i in range(6):
	t = s + t
	l.append(re.compile(t, re.UNICODE))
	if i % 2 == 1 :
		t = ':' + t

contestName = soup.findAll('a', href = search)
for name in contestName:
	if 'div' in str(name.parent):
		x = (name.parent.getText()).replace('Before contest','')
		for i in range(6):
			x = re.sub(l[i], '', x)
		names.append(str(x).strip(':'))

contestTimings = soup.findAll('span', {'class' : 'countdown'})
i = 0
for timing in contestTimings:
	if timing.text <= fifteen_minutes:
		Notify.init("Codeforces Reminder")
		notification = Notify.Notification.new(
			"Codeforces contest",
			names[i] + ' starts in less than 10 minutes! Taking you to the site...',
			"/home/hvk/Desktop/favicon.png"
		)
		notification.show()
		i += 1
		time.sleep(5)
		webbrowser.open_new(link)
