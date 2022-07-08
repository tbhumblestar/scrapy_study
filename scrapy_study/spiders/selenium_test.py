import scrapy

#selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#웹 드라이버관련
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumTestSpider(scrapy.Spider):
    name = 'selenium_test'
    allowed_domains = ['davelee-fun.github.io']
    
    #start_urls에서 https로 변경 및 마지막에 /삭제필요
    start_urls = ['https://davelee-fun.github.io/']
    
    def __init__(self):
        chromedriver = r'C:\Users\coloc\Desktop\chromedriver.exe'
        self.driver = webdriver.Chrome(service=Service(chromedriver))

    def parse(self, response):
        
        #selenium과 scrapy를 같이쓰는 게 좀 별로인 이유
        #기껏한 크롤링을, response.url얻어오는 데 만 싸용하고
        #selenium이 크롤링을 한번 더 함
        self.driver.get(response.url)
        time.sleep(2)
        elem = self.driver.find_elements(By.CSS_SELECTOR,".news")
        print(elem.text)
