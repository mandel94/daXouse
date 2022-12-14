from typing import Optional, Literal, Union

from scrapy.item import Item
from dataclasses import dataclass, field

@dataclass  
class House:
    '''Individual House''' 
    id: Optional[float] = field(default=None)
    title: Optional[str] = field(default=None)
    city: Optional[str] = field(default=None)   
    price: Optional[int] = field(default=None)
    rooms: Optional[int] = field(default=None)
    living_space: Optional[int] = field(default=None)
    bathrooms: Optional[int] = field(default=None)
    floor: Optional[str] = field(default=None)
    hasLift: Optional[bool] = field(default=False)
    has_balcony: Optional[bool] = field(default=None)
    has_terrace: Optional[bool] = field(default=None)
    is_luxury: Optional[bool] = field(default=False) 
    district: Optional[str] = field(default=None) 
    address: Optional[str] = field(default=None)
    enter_date: Optional[float] = field(default=None)
    agency: Optional[str] = field(default=None)
    descrizione: Optional[str] = field(default=None) 
    


