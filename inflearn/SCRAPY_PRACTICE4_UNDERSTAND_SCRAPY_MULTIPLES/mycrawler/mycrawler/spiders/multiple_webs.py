# -*- coding: utf-8 -*-
import scrapy


class MultipleWebsSpider(scrapy.Spider):
    name = 'multiple_webs'
    allowed_domains = ['davelee-fun.github.io']
    start_urls = ['http://davelee-fun.github.io/']

    def start_requests(self):
        yield scrapy.Request('http://davelee-fun.github.io/', self.parse)
        for i in range(2, 7):
            yield scrapy.Request('https://davelee-fun.github.io/page' + str(i), self.parse)

    def parse(self, response):
        print (response.url)
        pass
