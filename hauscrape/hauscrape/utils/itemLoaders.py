'''Item Loaders to populate Items'''

from scrapy.loader import ItemLoader
from itemloaders.processors import Identity, MapCompose

from utils.processors import get_digest

class HouseLoader(ItemLoader):
    ''' Load House Item'''
    # default processors
    default_input_processor = Identity()
    
    # id processors
    id_out = get_digest()

    # city processors
    

