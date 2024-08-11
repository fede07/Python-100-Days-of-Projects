from bs4 import BeautifulSoup
import requests

url = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")
print(url + date + "/")

response = requests.get(url=url + date + "/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(name="h3", id= "title-of-a-story")

for title in titles:
    print(title)