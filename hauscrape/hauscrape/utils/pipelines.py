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
import json
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter
from .items import House


class HousePipeline:
    ''''''

    def process_item(self, item, spider):
        ''''''
        if isinstance(item, House):
            return self.validate_item(item, spider)
        

    def validate_item(self, item, spider):
        '''Do Nothing'''
        return item



class JsonLinesExportPipeline:
    '''Write Items to Json file'''

    def open_spider(self, spider):
        ''''''
        self.exporters = {}
        self.jsonl_file = open(f'items.jsonl', 'wb')

    def close_spider(self, spider):
        ''''''
        for exporter in self.exporters.values():
            exporter.finish_exporting()
        self.jsonl_file.close()

    def _exporter_for_item(self, item):
        ''''''
        # This randomly generated id is only for testing purposes, and should
        # be removed and substituted by the real item id
        item_id = uuid.uuid4()
        exporter = JsonLinesItemExporter(self.jsonl_file)
        exporter.start_exporting()
        self.exporters[item_id] = exporter
        return exporter

    def process_item(self, item, spider):
        ''''''
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item


