import requests
from bs4 import BeautifulSoup

for n in range(1, 4) :
    raw = requests.get("https://news.ycombinator.com/news?p="+str(n),
                       headers = {'User-Agent' : "Mozilla/5.0"})

    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("tr.athing")

    for article in articles :
        title = article.select_one("a.storylink").text
        rank = article.select_one("span.rank").text
        source = article.select_one("span.sitestr").text

        print('제목 : ' + title)
        print('순위 : ' + rank)
        print('출처 : ' + source)

