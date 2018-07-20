import urllib.request
import time

t0 = time.time()
req = urllib.request.urlopen('http://www.example.com')
pageHTML = req.read()
t1 = time.time()
print (f"Total time to fetch {t1 - t0} secs")
