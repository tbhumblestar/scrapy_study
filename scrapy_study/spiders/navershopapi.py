import scrapy
import json
import re
from scrapy_study.items import openapiItem

class NavershopapiSpider(scrapy.Spider):
    name = 'navershopapi'
    # allowed_domains = ['openapi.naver.com']
    start_urls = ['	https://openapi.naver.com/v1/search/shop.json']
    #openapi는 반드시 https이고 마지막에 /가 없어야 함!

    def start_requests(self):
        client_id = '6FrD0SXswdDtoBKcqh1N'
        client_secret = 'L6QnliWQUa'

        headers = {
            'X-Naver-Client-Id':client_id,
            'X-Naver-Client-Secret':client_secret
        }
        query = 'iphone'
        for url in self.start_urls:
            yield scrapy.Request(url+ '?query='+query,self.parse,headers=headers)


    def parse(self, response):
        #response.text는 str임
        #따라서 사용하기 편하도록  json.loads를 사용해 dict로 바꿔준다
        datas = json.loads(response.text)

        #datas['items']가 실질적인 상품리스트임
        product_list = datas['items']

        for product in product_list:
            item = openapiItem()
            #정규표현식으로 데이터를 정리함
            product = re.sub('<\S+>','',product['title'])
            item['title'] = product
            yield item