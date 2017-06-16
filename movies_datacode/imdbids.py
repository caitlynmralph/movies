#test imdb api

import numpy as np
import os
import imdb
import csv

os.chdir('/Applications/MAMP/htdocs/project_2/horror_spreadsheets')

with open('/Applications/MAMP/htdocs/project_2/horror_spreadsheets/movies_ids.csv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    c = np.genfromtxt('Movies.tsv', delimiter="\t", dtype=str, skiprows=0)
    movies = c[:]

    print len(movies)

    # imdb_id = np.zeros([len(movies),1])
    # movies = np.reshape(movies, [len(movies),1])
    # movies_ids = np.concatenate([movies, imdb_id],axis=1)

    ia = imdb.IMDb()

    for i in range(0,len(movies)):
        s_result = ia.search_movie(movies[i])
        for item in s_result:
            if "(" in movies[i] and ")" in movies[i]:
                if item['long imdb canonical title'] == movies[i]:
                    print "movie has year", item['long imdb canonical title'], movies[i]
                    writer.writerow([movies[i], item.movieID])
                else:
                    print "movie has year",item['long imdb canonical title'], "No match"
                    writer.writerow([movies[i], "No match"])
            else:
                item_noyear = item['long imdb canonical title'].split('(', 1)[0].strip()
                if item_noyear == movies[i]:
                    print "movie doesn't have year", item_noyear, movies[i]
                    writer.writerow([movies[i], item.movieID])
                else:
                    print "movie doesn't have year",item_noyear, "No match"
                    writer.writerow([movies[i], "No match"])
            break