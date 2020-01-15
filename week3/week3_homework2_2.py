# 페이스북 로그인

from selenium import webdriver
import time

driver  = webdriver.Chrome("./chromedriver") # 크롬을 켠다.
driver.get("https://www.facebook.com/") # 해당하는 사이트에 접속한다

# 아이디 입력 받기
# 입력을 받지 않고 사전에 아이디와 비밀번호를 입력해도 좋습니다.
id = input('아이디를 입력해주세요 : ')
pw = input('패스워드를 입력해주세요 : ')

driver.find_element_by_css_selector("#email").send_keys(id) # id 입력햇
driver.find_element_by_css_selector("#pass").send_keys(pw) # pw 입력
time.sleep(1)

driver.find_element_by_css_selector("#u_0_e").click() # 로그인 버튼 클릭
driver.close()

# 네이버의 경우 자동입력 방지 문자를 통해
# 자동 로그인을 방지하고 있습니다.