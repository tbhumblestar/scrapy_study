# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class MycrawlerPipeline(object):
    def process_item(self, item, spider):
        if item['product_type'] == '행거도어 관련 상품 추천':
            raise DropItem('drop item for hanger door')
        else:
            return item
