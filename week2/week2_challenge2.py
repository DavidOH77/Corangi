import requests
from bs4 import BeautifulSoup

f = open('navernews.csv', 'w')

f.write('제목, 출처\n')

MAX = 100

for n in range(1, MAX, 10) :
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=호랑이&start="+str(n),
                       headers = {'User-Agent' : "Mozilla/5.0"})

    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("ul.type01 > li")

    for article in articles :
        title = article.select_one("a._sp_each_title").text.strip().replace( ','  , '' )
        source = article.select_one("span._sp_each_source").text.strip().replace( ','  , '' )

        f.write(title + ',' + source +  "\n")


f.close()
