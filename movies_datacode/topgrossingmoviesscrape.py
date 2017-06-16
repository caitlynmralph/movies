import re
import sys
import csv
from urllib2 import urlopen
from bs4 import BeautifulSoup
import numpy as np
import os

os.chdir('/Applications/MAMP/htdocs/project_2/movie_spreadsheets')

reload(sys)
sys.setdefaultencoding("utf-8")

with open('/Applications/MAMP/htdocs/project_2/movie_spreadsheets/scifi.csv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    url = "http://www.imdb.com/search/title?genres=sci_fi&sort=boxoffice_gross_us,desc"

    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    content = soup.find_all('div', {"class":"lister-item mode-advanced"})
    for item in content:
        title = item.find_all('a',href=re.compile('^/title/tt'))
        for thing in title:
            if np.shape(thing.contents) == (3,):
                        pass
            elif np.shape(thing.contents) == (1,):
                if 'bs4.element.Tag' not in str(type(thing.contents[0])):
                    imdb_id = thing['href'][9:16]
                    movie_id = thing.contents[0]

        gross = item.find_all('span', {"name": "nv"})
        for i in range(0, len(gross)):
            if i == 1 or i % 2 != 0:
                box_office = gross[i]['data-value'].replace(",", "")

        print movie_id,imdb_id,box_office
        writer.writerow([movie_id,imdb_id,box_office])

    for i in range(2, 11):
        url = "http://www.imdb.com/search/title?genres=sci_fi&sort=boxoffice_gross_us,desc&page="+str(i)+"&ref_=adv_nxt"

        html = urlopen(url).read()
        soup = BeautifulSoup(html, "lxml")

        content = soup.find_all('div', {"class": "lister-item mode-advanced"})
        for item in content:
            title = item.find_all('a', href=re.compile('^/title/tt'))
            for thing in title:
                if np.shape(thing.contents) == (3,):
                    pass
                elif np.shape(thing.contents) == (1,):
                    if 'bs4.element.Tag' not in str(type(thing.contents[0])):
                        imdb_id = thing['href'][9:16]
                        movie_id = thing.contents[0]

            gross = item.find_all('span', {"name": "nv"})
            for i in range(0, len(gross)):
                if i == 1 or i % 2 != 0:
                    box_office = gross[i]['data-value'].replace(",", "")

            print movie_id, imdb_id, box_office
            writer.writerow([movie_id, imdb_id, box_office])