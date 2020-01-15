import requests
from bs4 import BeautifulSoup
raw = requests.get('https://movie.naver.com/movie/running/current.nhn')

html = BeautifulSoup(raw.text, 'html.parser')

movie = html.select("dl.lst_dsc")

for m in movie:
    title = m.select_one('dt.tit a')
    score = m.select_one('div.star_t1 span.num')

    # info = m.select('dl.info_txt1 dd')
    # genre = info[0].select('a')
    # directors = info[1].select('a')
    # actors = info[2].select('a')

    genre = m.select('dl.info_txt1 dd:nth-of-type(1) a')
    directors = m.select('dl.info_txt1 dd:nth-of-type(2) a')
    actors = m.select('dl.info_txt1 dd:nth-of-type(2) a')

    print("="*50)
    print("제목 : ", title.text)

    print("=" * 50)
    print("평점 : ", score.text)

    print("=" * 50)
    print("장르 : ")
    for g in genre:
        print(g.text)

    print("=" * 50)
    print("감독 : ")
    for d in directors:
        print(d.text)
