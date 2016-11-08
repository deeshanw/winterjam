import string
import random
import urllib2
import re
import ctypes
 
def tickets():
		requestUrl = "http://www.radio1045.com/features/radio-1045-winter-jam-2016-1622/"
		pattern = " and more chances to win your way in. Keep checking back for your chance to get your FREE tickets to this show!"
		req = urllib2.Request(requestUrl)
		res = urllib2.urlopen(req)
		website = res.read()
		m = re.search(pattern, website)
		if m:
			pass
		else:
			ctypes.windll.user32.MessageBoxA(0, "Ticket download info available! Check http://www.radio1045.com/features/radio-1045-winter-jam-2016-1622/", "New Ticket Info!", 1)

tickets()
