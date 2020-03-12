from urllib import request
from bs4 import BeautifulSoup

content = request.urlopen("http://www.naver.com")
soup = BeautifulSoup(content, 'html.parser')

for data in soup.select("a"):
    print(data)
