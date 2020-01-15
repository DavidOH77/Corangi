import requests
from bs4 import BeautifulSoup

raw = requests.get("http://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

clips = html.select("div.cds_type")

for clip in clips :
    title = clip.select_one("dt.title")
    chn = clip.select_one('dd.chn')
    hit = clip.select_one("span.hit")
    like = clip.select_one("span.like")
    rank = clip.select_one("span.num")
    print(rank.text.strip()+"위")
    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
