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

    # if float(score.text) < 8.5:
    #    continue

    genre_all = m.select_one('dl.info_txt1 dd:nth-of-type(1) span.link_txt')

    if '액션' not in genre_all.text:
        continue
    print(title.text)