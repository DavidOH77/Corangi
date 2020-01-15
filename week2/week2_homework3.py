import requests
from bs4 import BeautifulSoup

for n in range(1,20) :
    raw = requests.get("https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q=호랑이&p="+str(n))

    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.cont_inner")

    for article in articles :
        title = article.select_one("div.cont_inner > div").text.strip()
        summary = article.select_one("div.cont_inner > p").text

        print('제목 : ' + title)
        print('요약 : ' + summary)