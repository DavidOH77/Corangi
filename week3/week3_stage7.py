from selenium import webdriver
import time

driver  = webdriver.Chrome("./chromedriver") # 크롬을 켠다.
driver.get("https://map.naver.com") # 해당하는 사이트에 접속한다
driver.find_element_by_css_selector("span.icon").click() # 홍보 문구 닫기
time.sleep(2)
driver.find_element_by_css_selector("a.link_navbar.search").click() # 검색 버튼 누르기
time.sleep(2)
driver.find_element_by_css_selector("div.search_box input").send_keys("치킨") # 검색어 입력
time.sleep(1)
driver.find_element_by_css_selector("a.link_place").click() # 검색어 결과 확인 버튼 클릭
time.sleep(2)

stores = driver.find_elements_by_css_selector("div.link_search") # 컨테이너 설정
for n in range(1, 5 ):
    time.sleep(1) # 페이지 이동했으니 잠시 지연
    for store in stores:
         name = store.find_element_by_css_selector\
             ("span.search_title_text").text # 제목 수집
         addr = store.find_element_by_css_selector\
             ('span.search_text.address').text # 주소 수집
         phone = store.find_element_by_css_selector\
             ('span.search_text.phone.ng-star-inserted').text # 전화 번호 수집
         print(name, addr, phone)

    # 페이지 이동하기
    page_bar = driver.find_elements_by_css_selector('div.pagination_area > *')
    page_bar[n+1].click()
driver.close()

# 다만 전화번호가 없는 치킨집 떄문에 에러발생!!