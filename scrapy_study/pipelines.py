from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter

class ScrapyStudyPipeline:
    def process_item(self, item, spider):
        if '행거' in item['recent_products_titles']:
            raise DropItem('행거관련 아이템 제거')
        else:            
            return item