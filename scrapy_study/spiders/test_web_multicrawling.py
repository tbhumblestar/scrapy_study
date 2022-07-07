import scrapy
from scrapy_study.items import ScrapyStudyItem

class TestWebMulticrawlingSpider(scrapy.Spider):
    name = 'test_web_multicrawling'
    allowed_domains = ['davelee-fun.github.io']
    # start_urls = ['http://davelee-fun.github.io/']

    def start_requests(self):
        #1페이지 
        yield scrapy.Request('http://davelee-fun.github.io/',self.parse)

        #해당 사이트의 웹페이지가 9쪽까지 잇음. 
        for i in range(2,9):
            yield scrapy.Request('http://davelee-fun.github.io/page'+str(i),self.parse)

    def parse(self, response):
        recent_products_titles = response.css('section.recent-posts a.text-dark::text').getall()
        recent_products_names = response.css('section.recent-posts h4.card-text::text').getall()

        for i,title in enumerate(recent_products_titles):
            item = ScrapyStudyItem()
            item['recent_products_titles'] = title.strip()
            #strip없으면 \n같은 게 데이터 끝에 달려있음
            item['recent_products_names'] = recent_products_names[i].strip()
            yield item

# json형태로 아이템 저장
# scrapy crawl test_web_multicrawling -o test_web_multicrawling.json -t json