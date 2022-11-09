from dataclasses import dataclass, field
from typing import Optional, Literal
from itemloaders.processors import MapCompose
from utils.processors import filter_intrinsic_prop

@dataclass  
class House:
    id
    city: str
    offered_for: Literal['for_sale', 'for_rent']
    price: int
    n_of_rooms: int
    district: str
    sub_district: str
    address: str
    active: bool
    enter_date: float
    agency: pd.Timestamp
    exit_date: Optional[float] = field(default=None)

    # id = scrapy.Field(
    #     input_processor=filter_intrinsic_prop()
    #     output_processor=
    # )

@dataclass
class HouseList:
    timestamp: float
    house: House