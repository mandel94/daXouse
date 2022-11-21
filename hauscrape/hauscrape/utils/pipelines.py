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

import uuid
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem

from .items import House


class HousePipeline:
    ''''''

    def process_item(self, item, spider):
        ''''''
        if isinstance(item, House):
            return self.validate_item(item, spider)
             
        

    def validate_item(self, item, spider):
        ''''''
        adapter = ItemAdapter(item)
        if not adapter['price']:
            raise DropItem(f"Item={item} is a group of houses/apartments.\
                             It has been dropped.")
        return item



class JsonLinesExportPipeline:
    '''Write Items to Json file'''

    def __init__(self):
        ''''''
        self.files = {}

    def open_spider(self, spider):
        ''''''
        self.file = open(f'items.json', 'wb')
        self.files[spider] = self.file
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        ''''''
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        ''''''
        self.exporter.export_item(item)
        return item


