# Ch_selenium/example/tutorial4.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # 또는 chromedriver.exe
driver.implicitly_wait(15)  # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

for i in range(100, 10000):
    url = 'https://opensea.io/assets/klaytn/0xe47e90c58f8336a2f24bcd9bcb530e2e02e1e8ae/' + \
        str(i)

    # 페이지 가져오기(이동)
    driver.get(url)
    time.sleep(1)

# # 요소 찾기 - 검색창찾고 키 전송

# refresh = driver.find_elements_by_xpath("//i[@value='refresh']")[0]
# refresh = driver.find_elements_by_class_name(
# "sc-1xf18x6-0")
    refresh = driver.find_elements_by_class_name(
        "sc-1xf18x6-0.sc-glfma3-0.hiIVBZ.gyCmAw.sc-1skvztv-0.fPnOUC")[0]
# class="sc-1xf18x6-0 sc-glfma3-0 hiIVBZ gyCmAw sc-1skvztv-0 fPnOUC"
#  sc-glfma3-0 hiIVBZ gyCmAw sc-1skvztv-0 fPnOUC
# search.send_keys('고슴도치')
# <div aria-hidden="true" pointer-events="none" class="sc-1xf18x6-0 sc-1twd32i-0 bMAZiO kKpYwv"><i size="22" value="refresh" class="sc-1gugx8q-0 fTvbZt material-icons">refresh</i></div>
# search.send_keys(Keys.ENTER)
    refresh.click()
    time.sleep(0.5)


# # 요소 찾기 - 지식백과에서 고슴도치 클릭
# posts = driver.find_elements_by_css_selector('a.tit')
# posts[0].click()
# time.sleep(2)
