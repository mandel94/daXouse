'''This file will set the standards for Item values.

Standards define constraints on the data representation of items, such as string 
formatting. They are useful to check that data is exctracted in the same format
independently from the data source / website. This is essential to aggregate 
data from those different sources. 

Data standards are defined using regualar expressions.

'''
import re
from abc import abstractmethod

from utils.constants import STRING_STANDARDS

# Instantiate dictionary of standards


class Standard(): 
    '''Class defining standards'''

    standards = {
    'city': STRING_STANDARDS['CITY'],
    'district': STRING_STANDARDS['DISTRICT'],
    'address': STRING_STANDARDS['ADDRESS'] 
    }

    def _get_standard(self):
        '''Get standard regex for `self.field`'''
        return Standard.standards[self.field]

    def __init__(self, field: str) -> None:
        self.field = field

    @abstractmethod
    def convert_to_standard(self, value):
        '''Conversion to standard depends on the specific real estate platform.
        
        The concrete implementation is platform-specific.
        '''
        pass
            
    def validate(self, value):
        ''''''
        # Return True / False if match / no match
        return re.search(value, self._get_standard())

