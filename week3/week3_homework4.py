# 인스타그램 댓글 크롤링

from selenium import webdriver
import time

# csv파일 만들기
f = open('insta_reply.csv', 'w', -1, "utf-8")

driver  = webdriver.Chrome("./chromedriver") # 크롬을 켠다.
driver.get("https://www.instagram.com/?hl=ko") # 해당하는 사이트에 접속한다
time.sleep(1)

# 로그인하기
# 보통 페이스북 계정을 이용하므로 이를 통해 로그인 해보겠습니다.

# 페이스북으로 로그인하기 버튼 누르기
driver.find_element_by_css_selector(" button.sqdOP.L3NKy.y3zKF:nth-of-type(1)").click()
time.sleep(1)

# 아이디 입력
id = input('페이스북 아이디를 입력해주세요 : ')
driver.find_element_by_css_selector("#email").send_keys(id) # id입력

# 패스워드 입력
pw = input('페이스북 패스워드를 입력해주세요 : ')
driver.find_element_by_css_selector("#pass").send_keys(pw) # pw입력

driver.find_element_by_css_selector("#loginbutton").click() # 로그인 버튼 클릭
time.sleep(2)

# 알림 설정창 닫기
driver.find_element_by_css_selector("div.mt3GC > button.aOOlW.HoLwm").click()
time.sleep(0.5)

# 검색하기
driver.find_element_by_css_selector("div.LWmhU._0aCwM > div > div").click() #검색버튼 누르기
search = input('검색어를 입력해주세요 : ')
driver.find_element_by_css_selector("div.LWmhU._0aCwM > input").send_keys(search) # 검색어 입력
time.sleep(2)
driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div:nth-child(4) > div.drKGC > div > a:nth-child(1)").click() #해쉬 태그와 합쳐진 검색어 누르기
time.sleep(4)

# 댓글 보기
cont = driver.find_elements_by_css_selector("div._9AhH0") # 컨테이너 설정
n = 0
for c in cont :

    # 횟수 정보 주기
    n = n+1
    if n == 13:
        break
    print(str(n)+'번째 게시글')
    f.write(str(n)+'번째 게시글'+'\n')
    print('')
    f.write('\n')

    c.click() #게시글 클릭하기
    time.sleep(1)

    # 게시글 주인공 아이디
    insta_id = driver.find_element_by_css_selector('h2._6lAjh > a').text.strip().replace(',','')
    print('인스타 아이디 :',insta_id)
    f.write('인스타 아이디 : ' + insta_id + "\n")
    f.write('\n')
    print('')

    # 인스타 내용
    main = driver.find_element_by_css_selector('div.C4VMK > span:nth-of-type(1)').text.strip().replace(',','')
    print('인스타 내용 :', main)
    f.write('인스타 내용 : ' + main + "\n")
    f.write('\n')
    print('')

    # 인스타 댓글단 아이디 선택자
    Repl_id = driver.find_elements_by_css_selector('div.C4VMK > h3 > a')

    # 댓글단 사람의 갯수 초기값 주기
    n1 = 0
    Repl_id_all = []
    # 모든 댓글단 사람 출력하기
    for r in Repl_id:
        n1 = n1 + 1
        r = r.text.strip().replace(',','')
        print('인스타 %d번째 댓글단 사람 :' % (n1), r)
        Repl_id_all.append(r)
        f.write('인스타 %d번째 댓글단 사람 :' % (n1) + r + "\n")
    f.write('\n')
    print('')

    # 인스타 댓글 선택자
    # 처음 것은 주인공이 단 게시글
    repl = driver.find_elements_by_css_selector('div.C4VMK > span')[1:]

    # 댓글의 횟수 초기값 주기
    n2 = 0
    repl_all = []
    # 모든 댓글 출력하기
    for r in repl:
            n2 = n2 + 1
            r = r.text.strip().replace(',','')
            print('인스타 %d번째 댓글 :' % (n2), r)
            repl_all.append(r)
            f.write('인스타 %d번째 댓글 :' % (n2) + r + "\n")
    print('')

    # ***********댓글이 없어도 딱히 오류가 나지는 않는다..!**************

    # 창을 닫아 다시 뒤로가기
    driver.find_element_by_css_selector('button.ckWGn').click()

    print('='*200)

    # 게시글마다 구분해주기
    f.write(''+'\n'+'다음 게시글 >>>'+'\n'+''+'\n')



f.close()
driver.close()