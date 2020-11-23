import requests
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
    print(full_list)
    for movie in movies:
        print(movie)
        #print(movie.text.strip())
yr2 = soup.find(id="2006")
#print(yr2)

curr = yr2
#print()

#while "multicol" not in curr:
#    print(curr.next_element)
#    curr = curr.next_element
#print(curr)
#allYears[0].find_all("a")