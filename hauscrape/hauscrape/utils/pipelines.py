'''Item Pipelines for processing Items

Item Pipelines can be used for:
    - validating items 
    - writing items (Feed exports is a better alternative)
    - ...

To know more, click here (https://docs.scrapy.org/en/latest/topics/item-pipeline.html)

'''

import json
from itemadapter import ItemAdapter

class HousePipeline:
    ''''''

    def process_item(self, item, spider):
        ''''''
        adapter = ItemAdapter(item)
        return item


class JsonWriterPipeline:
    '''Write Items to Json file for testing purposes'''
    def open_spider(self, spider):
        self.file = open('items.jsonl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item


