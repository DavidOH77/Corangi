import requests
from bs4 import BeautifulSoup
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

    reply = html_each.select("div.score_result li")

    print("평점과 댓글 : ")
    for r in reply:
        score = r.select_one("div.star_score em").text.strip()
        reply = r.select_one("div.score_reple p").text.strip()
        print(score, reply)

    print("=" * 50)