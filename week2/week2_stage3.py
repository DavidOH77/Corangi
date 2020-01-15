import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&query=호랑이",
                   headers = {'User-Agent' : "Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')
print(html)

articles = html.select("ul.type01 > li")

title = articles[0].select_one("a._sp_each_title").text

#print(title)

source = articles[0].select_one("span._sp_each_source").text

print(title +'\n' + source)