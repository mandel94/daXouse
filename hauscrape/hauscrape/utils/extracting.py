'''Functions for scraping raw data.

Final values to be loaded into Items are obtained with the following approach:
    1. Scrape the raw data;
    2. Refine the raw data;
    3. Validate the refined data;
    4. Load validated data into Items.

This file refers to point 1.
The steps for data extraction are the following:
    1.1 Select the html node(s) from which to extract data using Scrapy Spiders.
    1.2 Get the raw data from selected node(s), calling Scrapy methods such as 
        `get()` or `getall()`

Extracted raw data will be later passed to the refining functionalities for the 
data to be cleaned. 

'''