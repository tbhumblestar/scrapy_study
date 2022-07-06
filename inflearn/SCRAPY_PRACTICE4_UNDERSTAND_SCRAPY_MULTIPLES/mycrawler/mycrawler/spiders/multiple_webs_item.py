# -*- coding: utf-8 -*-
import scrapy
from mycrawler.items import MycrawlerItem


class MultipleWebsItemSpider(scrapy.Spider):
    name = 'multiple_webs_item'
    allowed_domains = ['davelee-fun.github.io']
    start_urls = ['http://davelee-fun.github.io/']

    def start_requests(self):
        yield scrapy.Request('http://davelee-fun.github.io/', self.parse)
        for i in range(2, 7):
            yield scrapy.Request('https://davelee-fun.github.io/page' + str(i), self.parse)

    def parse(self, response):
        product_types = response.css(
            'section.recent-posts div.card-body > h2 > a::text').getall()
        product_names = response.css(
            'section.recent-posts div.card-body > h4::text').getall()
        for index, product_type in enumerate(product_types):
            item = MycrawlerItem()
            print(product_type)
            item['product_type'] = product_type.strip()
            item['product_name'] = product_names[index].strip()
            yield item
