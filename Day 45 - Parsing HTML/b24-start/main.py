from bs4 import BeautifulSoup
import requests

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_= "titleline")
for article_tag in articles: 
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    article_upvote = soup.find(name="span", class_= "score").getText()

    print(article_text)
    print(article_link)
    print(article_upvote)