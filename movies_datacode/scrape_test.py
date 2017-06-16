# test web scrape

from lxml import html
import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.imdb.com/title/tt0077651/')
soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find_all('p')

print content

# for i in range(0,len(content)):
#     print content[i].get_text()