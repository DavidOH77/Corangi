from selenium import webdriver
import time

# 크롬 드라이버 실행
driver  = webdriver.Chrome("./chromedriver")

# 파파고 사이트 접속
driver.get("https://papago.naver.com")

# input 문장 받기
sentence = input('번역할 문장을 입력해주세요 : ')

# 문장 보내기
driver.find_element_by_css_selector("#sourceEditArea > label").send_keys(sentence) # 검색어 입력
time.sleep(1)

# 번역 버튼 누르기
driver.find_element_by_css_selector("#btnTranslate").click()
time.sleep(1)

# 번역 결과 불러오기
translate = driver.find_element_by_css_selector("#targetEditArea")
print(translate.text)
time.sleep(1)

driver.close()