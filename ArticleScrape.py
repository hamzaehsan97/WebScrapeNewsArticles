import requests
from bs4 import BeautifulSoup
keyword = input('Enter keyword:')

def returnArticles(keyword):
    page = requests.get('https://news.google.com/search?q='+keyword+'%20when%3A1y&hl=en-US&gl=US&ceid=US%3Aen')
    soup = BeautifulSoup(page.content, 'html.parser')
    weblinks = soup.find_all('article')
    pagelinks = []
    for link in weblinks[1:10]:
          url = link.contents[0].get('href')
          title = link.contents[1].find('a').getText()
          infoTuple = (('http://news.google.com'+url),title)
          pagelinks.append(infoTuple)
          return pagelinks

print(returnArticles(keyword))