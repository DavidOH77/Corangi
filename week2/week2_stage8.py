import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active
    print("불러오기 성공!")
    sheet.append(['', '']) # 공백으로 이전 데이터와 시각적 거리감 주기


except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(['제목', '출처'])
    print("신규 파일 생성")

MAX = 100

keyword = input("수집 키워드를 입력해주세요 : ")

for n in range(1, MAX, 10) :
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=" + keyword + "&start="+str(n),
                       headers = {'User-Agent' : "Mozilla/5.0"})

    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("ul.type01 > li")

    for article in articles :
        title = article.select_one("a._sp_each_title").text
        source = article.select_one("span._sp_each_source").text

        print(title +'\n' + source)
        sheet.append([title, source])

wb.save('navernews.xlsx')