'''Item Pipelines for processing Items

Item Pipelines can be used for:
    - validating items 
    - writing items (Feed exports is a better alternative)
    - ...

To know more, click here (https://docs.scrapy.org/en/latest/topics/item-pipeline.html)

'''

from itemadapter import ItemAdapter

class HousePipeline:
    ''''''

    def process_item(self, item, spider):
        ''''''
        adapter = ItemAdapter(item)
        return item