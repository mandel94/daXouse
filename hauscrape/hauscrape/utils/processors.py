'''Input and Output Processors for Item Loaders

Processors accept one (and only one) positional argument, which must be 
always an iterable. The output of those functions can be anything. Processors 
are defined for each field to be populated. Values returned by input processors 
are collected internally (in lists) and then passed to output processors to 
populate the fields.

'''

import re
import hashlib
from typing import List, Union
import logging

from .customExceptions import IdDigestError
from .custom_types import T
from .constants import GROUND_FLOOR_VALUE

def to_lowercase(value: str) -> str:
    '''Processor for string inputs. 
    
    Convert string to lowercase, plus manage missing values

    '''
    try:
        return value.lower()
    except:
        return None
    
def strip_ws(value: str) -> str:
    '''Processor for string inputs.
    
    Remove leading and ending spaces.

    '''
    try:
        return value.strip()
    except:
        return None

def remove_duplicate_ws(value: str) -> str:
    '''Processor for string inputs.

    Remove duplicate whitespaces.

    '''
    try:
        return ' '.join(value.split())
    except:
        return None

def remove_currency_symbols(price: str) -> str:
    '''Remove currency symbols from price'''
    try:
        special_symbols_pattern = r"[€$£]"
        return re.sub(special_symbols_pattern, '', price)
    except: 
        return None

def convert_price_to_int(price: str) -> int:
    '''Convert price to integer'''
    try:
        # Remove thousand and decimal separators
        price = price.replace('.', '')\
                     .replace(',', '')\
                     .replace('_', '')
        return int(price)
    except:
        return None

def convert_to_int(x: List[str]) -> int:
    ''''''
    try:
        return int(unlist_value(x))
    except:
        return None

def convert_to_bool(x: Union[List[str], None]) -> bool:
    ''''''
    try:
        return bool(x)
    except:
        return False

def process_floor(floor: Union[List[str], None]) -> Union[int, None]:
    '''Handle value assignment to floor.'''
    if floor:
        try:
            intermediate_floor = int(floor[0]) # to trigger exception
            return str(intermediate_floor)
        except:
            return handle_floor(floor[0])
    else:
        return None

def handle_floor(what_floor: str) -> str:
    ''''''
    if what_floor == 'T': # ground floor
        return GROUND_FLOOR_VALUE
    
def process_district(district: List[str]) -> str:
    ''''''
    return district

## Output processors

def unlist_value(x: list[T]) -> Union[T, None]:
    ''''''
    try:
        logging.info(f'{x}')
        if x[0] == 'NoLo':
            logging.debug('NoLo found')
        return x[0]
    except:
        return None


def get_digest(*intrinsic_props):
    '''Get house id from hashing a number of its intrinsic properties.

    Intrinsic properties to digest are specified in the devdocs of this package.
    The hashing algorithm is sha-256.
    
    Parameters
    ----------
    *intrinsic_props
        Variable lenght list of interinsic properties of an house.

    Returns
    -------
    str
        The identifier of the house, the result of hashing the concatenation of 
        its intrinsic properties. Sha-256 hash functions is used, and the id is 
        the hexadecimal representation of the final digest.

    Raises
    ------
    IdDigestError
        Raised for exceptions during digest of unique house identifier.

    '''
    m = hashlib.sha256()
    for prop in intrinsic_props:
        try:
            m.update(bytes(prop, 'utf-8'))
        except Exception:
            raise(IdDigestError(prop))
    return m.hexdigest()
