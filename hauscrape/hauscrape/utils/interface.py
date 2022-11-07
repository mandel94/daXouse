'''Interface for house intrinsic properties

The interface is a dictionary, whose key/value pairs map the intrinsic 
properties as scraped from the data sources/websites to a standard value of that
intrinsic property, or a function that will produce that standard value as an 
output.

'''

# Interface Functions

def standarizeFloor(floor: str) -> float:
    ''''''
    firstElement = floor[0]
    if firstElement == 'Piano':
        # Get second word
        secondElement = floor.split(' ')[1]
        if secondElement == 'terra':
            # Float representation of 'Piano terra'
            return(0)
        elif secondElement == 'rialzato':
            # Float representation of 'Piano rialzato'
            return(0.5)
    return(float(floor[0]))


intrinsicPropsInterface = {
    'immobiliare': {
        'floor': standarizeFloor
    },
    'idealista': {

    }
}


