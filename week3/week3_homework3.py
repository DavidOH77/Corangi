# 인스타그램 크롤링

from selenium import webdriver
import time

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
time.sleep(1)
driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div:nth-child(4) > div.drKGC > div > a:nth-child(1)").click() #해쉬 태그와 합쳐진 검색어 누르기
time.sleep(4)

# 게시글 보기
cont = driver.find_elements_by_css_selector("div._9AhH0") # 컨테이너 설정
n = 0
for c in cont :

    # 횟수 정보 주기
    n = n+1
    if n == 13:
        break
    print(str(n)+'번째 게시글')

    c.click() #게시글 클릭하기
    time.sleep(1)

    # 인스타 아이디 데이터
    insta_id = driver.find_element_by_css_selector('h2._6lAjh > a').text.strip()
    print('인스타 아이디 :',insta_id)

    # 인스타 내용
    main = driver.find_element_by_css_selector('div.C4VMK > span:nth-of-type(1)').text.strip()
    print('인스타 내용 :', main)

    # 창을 닫아 다시 뒤로가기
    driver.find_element_by_css_selector('button.ckWGn').click()

    print('='*200)

driver.close()