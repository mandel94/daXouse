'''Input and Output Processors for Item Loaders

Processors accept one (and only one) positional argument, which must be 
always an iterable. The output of those functions can be anything. Processors 
are defined for each field to be populated. Values returned by input processors 
are collected internally (in lists) and then passed to output processors to 
populate the fields.

Final values to be loaded into Items are obtained with the following approach:
    1. Scrape the raw data;
    2. Refine the raw data;
    3. Validate the refined data;
    4. Load validated data into Items.

This file refers to point 4. 
Once the data has been extracted (1.), refined (2.) and validated (3.) it is 
ready to be loaded in the Item.

''' 
import hashlib
from utils.customExceptions import IdDigestError


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