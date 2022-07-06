import scrapy
from scrapy_study.items import ScrapyStudyItem

class TestWebCrawlerSpider(scrapy.Spider):
    name = 'test_web_crawler'
    allowed_domains = ['davelee-fun.github.io']
    start_urls = ['http://davelee-fun.github.io/']

    def parse(self, response):
        recent_products_titles = response.css('section.recent-posts a.text-dark::text').getall()
        recent_products_names = response.css('section.recent-posts h4.card-text::text').getall()
        
        # print(recent_products_titles)
        # print(recent_products_names)

        for i,title in enumerate(recent_products_titles):
            item = ScrapyStudyItem()
            item['recent_products_titles'] = title.strip()
            #strip없으면 \n같은 게 데이터 끝에 달려있음
            item['recent_products_names'] = recent_products_names[i].strip()

            yield item

# json형태로 아이템 저장
# scrapy crawl test_web -o test_web.json -t json

