# -*- coding: utf-8 -*-
import scrapy
import json
import re
from mynaverapi.items import MynaverapiItem


class NavershopapiItemSpider(scrapy.Spider):
    name = 'navershopapi_item'
    allowed_domains = ['openapi.naver.com/v1/search/shop.json']
    start_urls = ['https://openapi.naver.com/v1/search/shop.json']

    def start_requests(self):
        client_id = 'fAVF9CDfRtalGQA1inQR'
        client_secret = 'qysaIU8I6i'
        header_params = {'X-Naver-Client-Id': client_id,
                         'X-Naver-Client-Secret': client_secret}
        query = 'iphone'
        for url in self.start_urls:
            yield scrapy.Request(url + '?query=' + query, headers=header_params)

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        for search_item in data['items']:
            item = MynaverapiItem()
            item['title'] = re.sub('<\S+>', '', search_item['title'])
            yield item
