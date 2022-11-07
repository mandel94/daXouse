'''Input and Output Processors for Item Loaders

Processors accept one (and only one) positional argument, which must be 
always an iterable. The output of those functions can be anything. Processors 
are defined for each field to be populated. Values returned by input processors 
are collected internally (in lists) and then passed to output processors to 
populate the fields.

''' 

## Input processors
def filter_intrinsic_prop(value):
    '''Check if an intrinsic properties satisfy all requirements.
    
    Intrinsic properties of an house is used to get the house identifier. We 
    must be sure that the intrinsic property is found through scraping, else 
    the identifier cannot be obtained, and the house is skipped'''


## Output processors
### get_digest
def get_digest(*intrinsic_props):
    '''Get house id from hashing a number of its intrinsic properties.

    Intrinsic properties to digest are specified in the devdocs of this package.
    
    Parameters
    ----------
    *intrinsic_props
        Variable lenght list of interinsic properties of an house.

    Returns
    -------
    str
        The identifier of the house, the result of hashing a concatenation of 
        its intrinsic properties.

    Raises
    ------
    

    '''
    