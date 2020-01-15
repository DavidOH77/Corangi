import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get('http://ticket2.movie.daum.net/Movie/MovieRankList.aspx')

html = BeautifulSoup(raw.text, 'html.parser')

movie = html.select("ul.list_boxthumb > li")
n = 0

for m in movie:

    # href를 이용해서 상세 페이지에 들어가기
    link = m.select_one('a.link_g')
    url = link.attrs['href']
    raw_each = requests.get(url)
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    # 링크 내의 영화 데이터 선택자 접근하기
    title = html_each.select_one('div.subject_movie > strong.tit_movie')
    score = html_each.select_one('div.subject_movie em.emph_grade')
    director = html_each.select_one('dd > a:nth-child(1)')
    actor = html_each.select_one('dd:nth-child(10) > a')
    genre = html_each.select_one('dl.list_movie.list_main > dd:nth-child(2)')

    n = n+1
    n1 = str(n)
    print(n1+'위')
    try :
        print(title.text.strip())
        print(score.text.strip())
        print(director.text.strip())
        print(actor.text.strip())
        print(genre.text.strip())
    except :
        print('링크가 존재하지 않습니다.')
    print('=' * 70)

