'''Item Loaders to populate Items'''

from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from ..utils.processors import to_lowercase, strip_ws, remove_duplicate_ws, \
                             get_digest, remove_currency_symbols


class HouseLoader(ItemLoader):
    ''' Load House Item'''
    # default processors
    default_input_processor = MapCompose(str.lower,
                                         strip_ws,
                                         remove_duplicate_ws
                                         )

    price_in = remove_currency_symbols

                                         