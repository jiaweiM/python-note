from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break, or do dome other "Plan B"
except URLError as e:
    print('The server could not be found!')
else:
    # 继续执行
    print("It Worked!")
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
