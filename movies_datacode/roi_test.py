import numpy as np
import os

os.chdir('/Applications/MAMP/htdocs/project_2/movie_spreadsheets')

genres = ["horror"]

c = np.genfromtxt('%s_dataset.csv' % (genres[g]), delimiter="\t", dtype=str, skiprows=0)
movies = c[:]

sixties = np.zeros([0,0])
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

    movie_id = movie_id[0][0]
    imdb_id = imdb_id[0][0]
    gross = gross[0][0]
    budget = budget[0][0]
    roi = roi[0][0]
    release_date = release_date[0][0]

    if release_date[3] == 6 and roi != 0:
        sixties = np.append(sixties,roi)
    elif release_date[3] == 7 and roi != 0:
        seventies = np.append(seventies, roi)
    elif release_date[3] == 8 and roi != 0:
        eighties = np.append(eighties, roi)
    elif release_date[3] == 9 and roi != 0:
        ninties = np.append(ninties, roi)
    elif release_date[3] == 0 and roi != 0:
        two_thousands = np.append(two_thousands, roi)
    elif release_date[3] == 1 and roi !=0:
        twentyten_plus = np.append(twentyten_plus, roi)

sixties = np.delete(sixties,(1))
seventies = np.delete(seventies,(1))
eighties = np.delete(eighties,(1))
ninties = np.delete(ninties,(1))
two_thousands = np.delete(two_thousands,(1))
twentyten_plus = np.delete(twentyten_plus,(1))

sixties_mean = np.mean(sixties)
seventies_mean = np.mean(seventies)
eighties_mean = np.mean(eighties)
ninties_mean = np.mean(ninties)
two_thousands_mean = np.mean(two_thousands)
twentyten_plus_mean = np.mean(twentyten_plus)

genre_numbers = [sixties_mean,seventies_mean,eighties_mean,ninties_mean,two_thousands_mean,twentyten_plus_mean,]

print genre_numbers
