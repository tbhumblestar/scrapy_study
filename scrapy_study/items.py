import scrapy

class ScrapyStudyItem(scrapy.Item):
    recent_products_titles = scrapy.Field()
    recent_products_names = scrapy.Field()

class openapiItem(scrapy.Item):
    title = scrapy.Field()


