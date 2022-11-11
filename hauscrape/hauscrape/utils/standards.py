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
    '''Class defining standards
    
    Examples
    --------
    >>> field = 'city'
    >>> value = 'milano'
    >>> # Standard for city field is that value must be lowercase
    >>> standard = Standard(field)
    >>> standard.validate(value)
    True

    '''

    standards = {
        'city': STRING_STANDARDS['CITY'],
        'district': STRING_STANDARDS['DISTRICT'],
        'address': STRING_STANDARDS['ADDRESS']
    }

    def __init__(self, field: str) -> None:
        ''''''
        self.field = field

    def _get_standard(self):
        '''Get standard regex for `self.field`'''
        return Standard.standards[self.field]

    def validate(self, value):
        '''Validate that value satisfies defined standards for its field'''
        # Return True / False if match / no match
        return re.search(self._get_standard(), value)
