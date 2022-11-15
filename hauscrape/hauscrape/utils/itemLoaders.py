'''Item Loaders to populate Items'''

from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from ..utils.processors import to_lowercase, strip_ws, remove_duplicate_ws, \
                             get_digest


class HouseLoader(ItemLoader):
    ''' Load House Item'''
    # default processors
    default_input_processor = MapCompose(to_lowercase,
                                         strip_ws,
                                         remove_duplicate_ws)
