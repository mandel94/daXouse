from dataclasses import dataclass, field
from typing import Optional, Literal
from itemloaders.processors import MapCompose
from utils.processors import filter_intrinsic_prop

import pandas as pd

@dataclass  
class House:
    id: str
    city: str
    offered_for: Literal['for_sale', 'for_rent']
    n_of_rooms: int
    district: str
    sub_district: str
    address: str
    active: bool
    enter_date: pd.Timestamp
    agency: pd.Timestamp
    exit_date: Optional[pd.Timestamp] = field(default=None)

    # id = scrapy.Field(
    #     input_processor=filter_intrinsic_prop()
    #     output_processor=
    # )
