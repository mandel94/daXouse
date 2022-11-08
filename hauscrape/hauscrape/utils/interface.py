'''Interface for extracting, refining and validating data.

Final values to be loaded into Items are obtained with the following approach:
1. Scrape the raw data;
2. Refine the raw data;
3. Validate the refined data;
4. Load validated data into Items.

The HauscrapeInterface will provide functionalities for implementing all these
steps

'''