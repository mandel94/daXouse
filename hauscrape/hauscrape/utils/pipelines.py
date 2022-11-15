'''Item Pipelines for processing Items

Item Pipelines can be used for:
    - validating items 
    - writing items (Feed exports is a better alternative)
    - ...

To know more, click here (https://docs.scrapy.org/en/latest/topics/item-pipeline.html)

Example of pipeline application with signals 
    --> https://github.com/dm03514/CraigslistGigs/blob/master/craigslist_gigs/pipelines.py

Scrapy, Python: Multiple Item Classes in one pipeline?
    --> https://stackoverflow.com/questions/32743469/scrapy-python-multiple-item-classes-in-one-pipeline

'''

import json
from itemadapter import ItemAdapter
from .items import House

class HousePipeline:
    ''''''

    def process_item(self, item, spider):
        ''''''
        if isinstance(item, House):
            return self.validate_item(item, spider)
        # adapter = ItemAdapter(item)

    def validate_item(self, item, spider):
        '''Do Nothing'''
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


