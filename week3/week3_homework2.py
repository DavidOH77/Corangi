# 네이버 로그인

from selenium import webdriver
import time

driver  = webdriver.Chrome("./chromedriver") # 크롬을 켠다.
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com") # 해당하는 사이트에 접속한다

# 아이디 입력 받기
# 입력을 받지 않고 사전에 아이디와 비밀번호를 입력해도 좋습니다.
id = input('아이디를 입력해주세요 : ')
pw = input('패스워드를 입력해주세요 : ')

driver.find_element_by_css_selector("#id").send_keys(id) # id 입력
driver.find_element_by_css_selector("#pw").send_keys(pw) # pw 입력
time.sleep(1)

driver.find_element_by_css_selector("#log\.login").click() # 로그인 버튼 클릭

# 네이버의 경우 자동입력 방지 문자를 통해
# 자동 로그인을 방지하고 있습니다.
# 따라서 여기까지는 실행이 될지라도 로그인 후에 넘어가는 건 어려울 수 있습니다.

driver.close()
