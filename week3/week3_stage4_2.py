import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
raw = requests.get('https://movie.naver.com/movie/running/current.nhn')

html = BeautifulSoup(raw.text, 'html.parser')

movie = html.select("dl.lst_dsc")

for m in movie:
    title = m.select_one('dt.tit a')
    print("제목 :", title.text)

    url = title.attrs["href"]
    #print(url)
    #print("=" * 50)

    raw_each = requests.get("https://movie.naver.com"+url)
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    img = html_each.select_one("div.mv_info_area div.poster img")
    src = img.attrs["src"]

    urlretrieve(src, "img/" + title.text[:4] + ".png")

    print("+"*50)
    print(title.text, "포스터 저장완료" )