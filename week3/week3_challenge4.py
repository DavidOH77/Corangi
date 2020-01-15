# 구글지도 데이터 수집기

from selenium import webdriver
import time

driver  = webdriver.Chrome("./chromedriver") # 크롬을 켠다.
driver.get("https://www.google.com/maps") # 해당하는 사이트에 접속한다

# 검색어 입력 받기
input = input('검색어를 입력해주세요 : ')

driver.find_element_by_css_selector("#gs_lc50 > #searchboxinput").send_keys(input) # 검색창에 input 입력
time.sleep(1)

driver.find_element_by_css_selector("#searchbox-searchbutton").click() # 검색어 결과 확인 버튼 클릭
time.sleep(1)


# 페이지 이동시 잠시 지연
time.sleep(1)
stores = driver.find_elements_by_css_selector("div.section-result") # 컨테이너 설정

# whlie True를 이용하면 무한 반복 (break를 통해서만 빠져나갈 수 있다)
while True :

    # 번호를 매기기 위해 초기에 저장할 공간을 for문 밖에 준다.
    n = 0

    for store in stores:
        name = store.find_element_by_css_selector("h3 > span").text # 제목 수집

        # 주소 수집
        # 주소가 없는 경우 에러가 발생하므로 예외 처리
        try:
            addr = store.find_element_by_css_selector('span.section-result-location').text
        except:
            addr = '주소 불명'

        # 평점 수집
        # 평점은 존재하지 않는 경우도 있으므로 예외 처리를 해준다.
        try:
            score = store.find_element_by_css_selector('span.section-result-rating > span').text
        except:
            score = '평점 없음'

        # 번호 매기기
        n = n+1

        print(str(n)+'번째 가게')
        print('상호명 :', name)
        print('주소 :', addr)
        print('평점 :', score)
        print('='*70)



    # 페이지 이동하기
    page_bar = driver.find_element_by_css_selector('#n7lv7yjyC35__section-pagination-button-next > span')

    # 페이지가 마지막에 도달한 경우 멈추기
    try:
        page_bar.click()

    except:
        print('수집완료!')
        # 수집이 완료되었으므로 빠져나가기
        break

driver.close()