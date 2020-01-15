# f = open('hitsong.csv', 'w')
#
# singers = ['박정현', '임창정', 'izi', '아이유']
#
# songs = ['꿈에', '소주한잔', ' 응급실', '좋은날']
#
# for i  in range(len(singers)):
#     f.write(singers[i] + ',' + songs[i] + '\n')
#
# f.close()



import requests
from bs4 import BeautifulSoup

f = open('navertv.csv', 'w')

f.write('제목, 채널명, 재생 수 , 좋아요 수\n')

raw = requests.get("http://tv.naver.com/r")

html = BeautifulSoup(raw.text, "html.parser")

clips = html.select("div.cds_type")

for clip in clips :
    title = clip.select_one("dt.title").text.strip().replace( ','  , '' )
    chn = clip.select_one('dd.chn').text.strip().replace( ','  , '' )

    hit = clip.select_one("span.hit").text.strip().replace( ','  , '' )
    hit = hit[4:]

    like = clip.select_one("span.like").text.strip().replace( ','  , '' )
    like = like[5:]

    rank = clip.select_one("span.num").text.strip().replace( ','  , '' )
    f.write(title + ',' + chn + ',' + hit + ',' + like + "\n")


f.close()
