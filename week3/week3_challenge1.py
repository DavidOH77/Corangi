import requests
from bs4 import BeautifulSoup

# 홈페이지 접근
raw = requests.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth')

# 파싱
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 입력
movies = html.select('div.list_item')

# 컨테이너 1개당 내부의 정보 얻기
for movie in movies:

    # 제목 데이터 얻고 텍스트 변환
    title = movie.select_one('h4 > a').text.strip()

    # 평점 데이터 얻고 텍스트 변환
    # 평점 데이터가 존재하지 않으면 오류가 발생하기 때문에 예외처리로 오류 발생을 막아준다.
    # 그리고 오류 발생시 평점이 존재하지 않는다고 말해준다.

    # 평점이 있는지 없는지 모르므로 평점 데이터 얻기 시도
    try :
        score = movie.select_one('span.value')
        score = score.text.strip()
    # 평점이 없다면 아래의 문구를 출력
    except AttributeError:
        score = '평점이 존재하지 않습니다.'

    # 감독 데이터 얻고 리스트에 저장하기
    # 감독 데이터에 | 라는 텍스트도 포함되기 때문에 없에준다.

    # 감독 데이터에 관한 선택자로 데이터 불러오기
    directors = movie.select('div.txt-block > span')
    # 빈 리스트 만들어주기
    directors_all = []
    # | 를 제외한 텍스트만 리스트에 저장
    for d in directors :
        if not d.text == '|':
            d = d.text.strip()
            directors_all.append(d)

    # 감독 데이터와 마찬가지로 배우 데이터 얻어오기
    actors = movie.select('div.txt-block > a')
    actors_all = []
    for a in actors:
        if not a.text == '|':
            a = a.text.strip()
            actors_all.append(a)

    # 감독 데이터와 마찬가지로 장르 데이터 얻어오기
    genres = movie.select('p.cert-runtime-genre > span')[1:]
    genres_all = []
    for g in genres:
        if not g.text == '|':
            g = g.text.strip()
            genres_all.append(g)

    # Action이라는 장르에 속하지 않는 경우 아래에 있는 출력문을 실행하지 않고
    # contiune를 통해서 다음 차례로 넘어가기
    if 'Action' not in genres_all:
        continue

    # 얻어낸 데이터들을 출력하기
    print('제목 : ', title)
    print('평점 : ', score)
    # 리스트의 [ , , ] 와 같은 대괄호 없에기
    print('감독 : ', ", ".join( [str(i) for i in directors_all] ) )
    # 위와 마찬가지로 리스트의 대괄호 없에기
    print('배우 : ', ", ".join( map( str, actors_all ) ) )
    print('장르 : ', ', '.join( map( str, genres_all ) ) )

    print('='*70)

