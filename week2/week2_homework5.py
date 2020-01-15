import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("daumnews_2.xlsx")
    sheet = wb.active
    print("불러오기 성공!")
    sheet.append(['','', '']) # 공백으로 이전 데이터와 시각적 거리감 주기


except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(['검색어', '제목', '요약'])
    print("신규 파일 생성")

keyword = input('검색어를 입력해 주세요 : ')

for n in range(1,20) :
    raw = requests.get("https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q=" + keyword  + "&p="+str(n))

    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.cont_inner")

    for article in articles :
        title = article.select_one("div.cont_inner > div").text.strip()
        summary = article.select_one("div.cont_inner > p").text

        print('제목 : ' + title)
        print('요약 : ' + summary)
        sheet.append([keyword, title, summary])

wb.save('daumnews_2.xlsx')