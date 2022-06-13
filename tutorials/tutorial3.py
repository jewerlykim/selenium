# Ch_selenium/example/tutorial3.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # 또는 chromedriver.exe
driver.implicitly_wait(15)  # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get('https://www.google.co.kr')
driver.get('https://www.youtube.com/c/반원')
driver.get('https://www.naver.com')

# 이전 창으로 이동 2번하기
driver.back()
driver.back()

# 다음 창으로 2번 이동하기
driver.forward()
driver.forward()

# 3초후 종료
time.sleep(3)
driver.quit()  # 웹 브라우저 종료. driver.close()는 탭 종료
