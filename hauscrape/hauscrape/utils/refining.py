'''This class refines data during scraping.

Final values to be loaded into Items are obtained with the following approach:
    1. Scrape the raw data;
    2. Refine the raw data;
    3. Validate the refined data;
    4. Load validated data into Items.

This file refers to point 2. 
Refining functions get the raw data and applies some transformations to it. The 
refined data is later passed on to validating functions to verify that it 
satisfies expectations for inclusion in the final Item.  
    
'''

