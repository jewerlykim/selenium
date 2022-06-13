# Ch_selenium/example/tutorial4.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # 또는 chromedriver.exe
driver.implicitly_wait(15)  # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get('https://www.naver.com')

# 요소 찾기 - 검색창찾고 키 전송
search = driver.find_element_by_css_selector('#query')
search.send_keys('고슴도치')
search.send_keys(Keys.ENTER)
time.sleep(2)

# 요소 찾기 - 지식백과에서 고슴도치 클릭
posts = driver.find_elements_by_css_selector('a.tit')
posts[0].click()
time.sleep(2)
