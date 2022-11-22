'''Item Loaders to populate Items'''

from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, Identity, Compose
from ..utils.processors import to_lowercase, strip_ws, remove_duplicate_ws,\
                               remove_currency_symbols, convert_price_to_int,\
                               unlist_value, convert_to_int, convert_to_bool,\
                               process_floor


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

    rooms_in = convert_to_int
    living_space_in = convert_to_int
    bathrooms_in = convert_to_int
    floor_in = process_floor
    is_luxury_in = convert_to_bool

    default_output_processor = unlist_value




                                         