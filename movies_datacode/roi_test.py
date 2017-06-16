import numpy as np
import os

os.chdir('/Applications/MAMP/htdocs/project_2/movie_spreadsheets')

genres = ["horror"]

c = np.genfromtxt('%s_cleaned.csv' % (genres[0]), delimiter="\t", dtype=str, skiprows=1)
movies = c[:]

seventies = np.zeros([0, 0])
eighties = np.zeros([0, 0])
ninties = np.zeros([0, 0])
two_thousands = np.zeros([0,0])
twentyten_plus = np.zeros([0,0])

for i in range(0,len(movies)):
    movie_id = movies[i:i+1,0:1]
    imdb_id = movies[i:i+1,1:2]
    gross = movies[i:i + 1, 2:3]
    budget = movies[i:i + 1, 3:4]
    roi = movies[i:i+1,4:5]
    release_date = movies[i:i+1,5:6]

    movie_id = movie_id[0][0].replace('"',"")
    imdb_id = imdb_id[0][0].replace('"',"")
    gross = gross[0][0].replace('"',"")
    budget = budget[0][0].replace('"',"")
    roi = roi[0][0].replace('"',"")
    release_date = release_date[0][0].replace('"',"")

    if release_date[2] == "7" and roi != 0:
        seventies = np.append(seventies, float(roi))
    elif release_date[2] == "8" and roi != 0:
        eighties = np.append(eighties, float(roi))
    elif release_date[2] == "9" and roi != 0:
        ninties = np.append(ninties, float(roi))
    elif release_date[2] == "0" and roi != 0:
        two_thousands = np.append(two_thousands, float(roi))
    elif release_date[2] == "1" and roi !=0:
        twentyten_plus = np.append(twentyten_plus, float(roi))
    else:
        pass

seventies_mean = np.mean(seventies)
eighties_mean = np.mean(eighties)
ninties_mean = np.mean(ninties)
two_thousands_mean = np.mean(two_thousands)
twentyten_plus_mean = np.mean(twentyten_plus)

genre_numbers = [seventies_mean,eighties_mean,ninties_mean,two_thousands_mean,twentyten_plus_mean]

print genre_numbers
