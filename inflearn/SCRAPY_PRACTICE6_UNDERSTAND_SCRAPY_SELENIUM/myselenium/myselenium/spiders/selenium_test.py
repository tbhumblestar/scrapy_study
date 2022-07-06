# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
# [2022.06.30] find_element_by_() 함수는 find_element(By., ) 과 같은 형태로 함수가 변경됨에 따른 추가 코드
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumTestSpider(scrapy.Spider):
    name = 'selenium_test'
    allowed_domains = ['davelee-fun.github.io/blog/TEST/index.html']
    start_urls = ['https://davelee-fun.github.io/blog/TEST/index.html']

    def __init__(self):
        # chromedriver = 'C:/dev_python/Webdriver/chromedriver.exe' # 윈도우
        chromedriver = '/usr/local/Cellar/chromedriver/chromedriver'  # 맥
        headlessoptions = webdriver.ChromeOptions()
        headlessoptions.add_argument('headless')
        # [2022.06.30] webdriver.Chrome 인자가 변경됨에 따른 추가 코드
        # self.driver = webdriver.Chrome(chromedriver, options=headlessoptions)
        self.driver = webdriver.Chrome(service=Service(
            chromedriver), options=headlessoptions)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)

        # [2022.06.30] find_element_by_() 함수는 find_element(By., ) 과 같은 형태로 함수가 변경됨에 따른 추가 코드
        # elem = self.driver.find_element_by_css_selector(".news")
        elem = self.driver.find_element(By.CSS_SELECTOR, ".news")

        print(elem.text)
        pass
