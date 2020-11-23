import requests
import csv
import justwatch
from justwatch import JustWatch
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Traverse_City_Film_Festival",
)
soup = BeautifulSoup(response.content, 'html.parser')


years = list(range(2005, 2019))
print(years)

#find out where streaming
#manually set header to avoid api error
justwatch.justwatchapi.HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
just_watch = JustWatch(country='US')

for year in years:
    full_list = soup.find(id=year).findNext(class_="multicol")
    links = full_list.find_all("a")
    movies = full_list.find_all("li")
    stripped_links = []
    stripped_movies = []
    where_watch = []
    #print(full_list)
    for movie in movies:
        #print(movie)
        watch = []
        link = movie.find("a")
        title = movie.text.strip()
        if title.find(' - ') != -1:
            title = title[:title.find(' - ')]
        elif title.find(' — ') != -1:
            title = title[:title.find(' — ')]
        elif title.find(' — ') != -1:
            title = title[:title.find(' — ')]
        if "Shorts" not in title:
            stripped_movies.append(title)
        if link != None:
            link = "https://en.wikipedia.org" + link['href']
        else:
            link = ""
        stripped_links.append(link)
        #results = just_watch.search_for_item(query=title)
        
        try:
            continue
            #offers = results['items'][0]['offers']
            #for offer in offers:
                #if offer['monetization_type'] == 'flatrate':
                    #print("streaming: " + offer['urls']['standard_web'])
                    #watch.append(offer['urls']['standard_web'])
                #elif offer['monetization_type'] == 'rent':
                    #print("rent: " + offer['urls']['standard_web'])
            #watch = list(dict.fromkeys(watch))
        except KeyError:
            watch = []
        except IndexError:
            watch = []
        #print(title)
        #print(watch)
        where_watch.append(watch)
        
    #print(stripped_movies)
    #print(stripped_links)
    csv_name = str(year) + ".csv"
    with open(csv_name, 'w', newline='') as csvfile:
        movie_writer = csv.writer(csvfile, delimiter=',')
        movie_writer.writerow(stripped_movies + stripped_links + where_watch)
        
#test query
#results = just_watch.search_for_item(query='the matrix')
#print(results['items'][0]['offers'])
#offers = results['items'][0]['offers']

#for offer in offers:
#    print(offer['monetization_type'])
#    if offer['monetization_type'] == 'flatrate':
#        print(offer['urls']['standard_web'])

