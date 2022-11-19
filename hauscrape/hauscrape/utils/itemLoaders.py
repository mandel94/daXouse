'''Item Loaders to populate Items'''

from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, Identity
from ..utils.processors import to_lowercase, strip_ws, remove_duplicate_ws,\
                               remove_currency_symbols, convert_price_to_int


class HouseLoader(ItemLoader):
    ''' Load House Item'''
    # default processors
    default_input_processor = MapCompose(to_lowercase,
                                         remove_duplicate_ws,
                                         strip_ws)
                                         
    price_in = MapCompose(remove_currency_symbols,
                          to_lowercase,
                          remove_duplicate_ws,
                          strip_ws,
                          convert_price_to_int)

# class HouseCollectionLoader(ItemLoader):
#     ''''''
#     default_input_processor = Identity()


                                         