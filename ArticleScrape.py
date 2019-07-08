import requests
from bs4 import BeautifulSoup
companyName = input('Enter Company name:')
page = requests.get('https://news.google.com/search?q='+companyName+'%20when%3A1y&hl=en-US&gl=US&ceid=US%3Aen')
soup = BeautifulSoup(page.content, 'html.parser')

weblinks = soup.find_all('article')
pagelinks = []
for link in weblinks[1:10]:
      urlLink = link
      url = link.contents[0].get('href')
      title = link.contents[1].find('a').getText()
      infoTuple = (('http://news.google.com'+url),title)
      pagelinks.append(infoTuple)
print(pagelinks)
