import requests
from bs4 import BeautifulSoup

raw = requests.get("http://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")
#print(html)

clips = html.select("div.inner")
#print(clips)
#print(clips[0])

title = clips[0].select_one("dt.title")
#print(title)
#print(title.text)
chn = clips[0].select_one('dd.chn')
hit = clips[0].select_one("span.hit")
like = clips[0].select_one("span.like")

# print(title.text.strip())
# print(chn.text.strip())
# print(hit.text.strip())
# print(like.text.strip())

for clip in clips :
    title = clip.select_one("dt.title")
    chn = clip.select_one('dd.chn')
    hit = clip.select_one("span.hit")
    like = clip.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
