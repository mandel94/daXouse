'''Input and Output Processors for Item Loaders

Processors accept one (and only one) positional argument, which must be 
always an iterable. The output of those functions can be anything. Processors 
are defined for each field to be populated. Values returned by input processors 
are collected internally (in lists) and then passed to output processors to 
populate the fields.

'''

import re
import hashlib

from ..utils.customExceptions import IdDigestError

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





## Output processors
### get_digest
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
