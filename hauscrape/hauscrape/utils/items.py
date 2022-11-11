from dataclasses import dataclass, field
from typing import Optional, Literal
from itemloaders.processors import MapCompose
from utils.processors import filter_intrinsic_prop

@dataclass  
class House:
    offered_for: Literal['for_sale', 'for_rent']
    id: Optional[float] = field(default=None)
    title: Optional[str] = field(default=None)
    city: Optional[str] = field(default=None)
    price: Optional[int] = field(default=None)
    n_of_rooms: Optional[int] = field(default=None)
    living_space: Optional[int] = field(default=None)
    bathrooms: Optional[int] = field(default=None)
    hasLift: Optional[bool] = field(default=None)
    has_balcony: Optional[bool] = field(default=None)
    has_terrace: Optional[bool] = field(default=None)
    district: Optional[str] = field(default=None) 
    address: Optional[str] = field(default=None)
    enter_date: Optional[float] = field(default=None)
    agency: Optional[str] = field(default=None)
    descrizione: Optional[str] = field(default=None)  
    exit_date: Optional[float] = field(default=None)
    
