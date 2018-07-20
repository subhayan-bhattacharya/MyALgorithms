import urllib.request
import time
from bs4 import BeautifulSoup

t0 = time.time()
req = urllib.request.urlopen('http://www.example.com')
t1 = time.time()
print(f"Total time to fetch {t1 - t0} secs")
soup = BeautifulSoup(req.read(), "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))

t2 = time.time()
print(f"Total execution time {t2 - t0}")


