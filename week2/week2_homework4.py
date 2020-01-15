import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['순위', '제목', '저자'])
print("신규 파일 생성")

for n in range(1, 4) :
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page"+str(n),
                       headers = {'User-Agent' : "Mozilla/5.0"})

    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select('#content > div > ul > li')

    for book in books :
        title = book.select_one("#content > div > ul > li > a > strong").text
        rank = book.select_one("span.num").text.strip()
        writer = book.select_one("span.writer").text.strip()

        print('제목 : ' + title)
        print('순위 : ' + rank)
        print('저자 : ' + writer)

        sheet.append([rank, title, writer])

wb.save('naverEbook.xlsx')