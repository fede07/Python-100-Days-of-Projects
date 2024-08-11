import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")

titles = soup.find_all(name="h3", class_="title")
for title in titles[::-1]:
    title_text = title.getText()
    print(title_text)

with open("movies.txt", mode="a", encoding="UTF-8") as movies_file:
    for title in titles[::-1]:
        title_text = title.getText()
        movies_file.write(title_text+"\n")
    
    
