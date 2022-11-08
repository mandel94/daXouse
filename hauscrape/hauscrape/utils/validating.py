'''Function for validating refined scraped values.

Final values to be loaded into Items are obtained with the following approach:
    1. Scrape the raw data;
    2. Refine the raw data;
    3. Validate the refined data;
    4. Load validated data into Items.

This file defines validations functions relating to point 3.
For each field, we outline an expectation of its refined value.
That expectation is used in the validation funtion for that field. If the value 
satisfy the expectation, the validation function will return true.

'''

def validateFloor(floor: str) -> str:
    '''Floor is an intrinsic property'''
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


