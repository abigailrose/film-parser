import requests
import csv
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Traverse_City_Film_Festival",
)
soup = BeautifulSoup(response.content, 'html.parser')


years = list(range(2005, 2019))
print(years)

for year in years:
    full_list = soup.find(id=year).findNext(class_="multicol")
    links = full_list.find_all("a")
    movies = full_list.find_all("li")
    stripped_links = []
    stripped_movies = []
    #print(full_list)
    for movie in movies:
        #print(movie)
        link = movie.find("a")
        stripped_movies.append(movie.text.strip())
        if link != None:
            link = "https://en.wikipedia.org" + link['href']
        else:
            link = ""
        stripped_links.append(link)
    #print(stripped_movies)
    #print(stripped_links)
    csv_name = str(year) + ".csv"
    with open(csv_name, 'w', newline='') as csvfile:
        movie_writer = csv.writer(csvfile, delimiter=',')
        movie_writer.writerow(stripped_movies + stripped_links)