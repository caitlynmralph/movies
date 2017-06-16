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

with open('/Applications/MAMP/htdocs/project_2/movie_spreadsheets/scifi_dataset.csv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)


    c = np.genfromtxt('scifi.csv', delimiter="\t", dtype=str, skiprows=0)
    movies = c[:]

    for i in range(0,len(movies)):
        movie_id = movies[i:i+1,0:1]
        imdb_id = movies[i:i+1,1:2]
        gross = movies[i:i+1,2:3]

        movie_id = movie_id[0][0]
        imdb_id = imdb_id[0][0]
        gross = gross[0][0]

        print movie_id

        url = "http://www.imdb.com/title/tt"+imdb_id+"/business"

        print url

        html = urlopen(url).read()
        soup = BeautifulSoup(html, "lxml")

        budget = 0

        for elem in soup(text=re.compile(r' \(estimated\)')):
            print elem
            if "$" in elem:
                elem = elem.split('(estimated')[0]
                thing = elem.replace("(", "").replace(")", "").replace("$", "").replace(",", "").replace(" ", "")
                # find all characters in the string that are numeric.
                thing = re.search(r'\d+', thing)
                budget = thing.group()  # retrieve numeric string

        url = "http://www.imdb.com/title/tt"+imdb_id
        print url

        html = urlopen(url).read()
        soup = BeautifulSoup(html, "lxml")

        item = soup.find("meta", {"itemprop": "datePublished"})  # meta content="Free" itemprop="price"
        if item != None:
            date = item['content']
        else:
            date = 0

        if budget != 0 and date !=0:
            print movie_id, imdb_id, gross, budget, float(gross)/float(budget), date
            writer.writerow([movie_id, imdb_id, gross, budget, float(gross)/float(budget), date])
        else:
            print movie_id, imdb_id, gross, budget, 0, date
            writer.writerow([movie_id, imdb_id, gross, budget, 0, date])