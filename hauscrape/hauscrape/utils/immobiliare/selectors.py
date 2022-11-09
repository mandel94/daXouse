# Scrapy selectors
XPATH_ONSALE_LIST_IMMOBILIARE = '//ul[@data-cy="result-list"]/li[@class="nd-list__item in-realEstateResults__item"]'
XPATH_PRICE_IMMOBILIARE = '//li[@class="in-feat__item--main"]/text()'
XPATH_N_OF_ROOMS_IMMOBILIARE = '//li[@aria-label="locali"]/text()'

# HTML attributes

## Scrape the offer price
PRICE_ATTRIBUTE = 'class'
PRICE_ATTRIBUTE_VALUE = 'in-realEstateListCard__features--range'

## Scrape the number of rooms
ROOMS_ATTRIBUTE = 'aria-label'
ROOMS_ATTRIBUTE_VALUE = 'locali'

## Scrape the living space of the apartment
LIVING_SPACE_ATTRIBUTE = 'aria-label'
LIVING_SPACE_ATTRIBUTE_VALUE = 'superficie'

## Scrape the number of bathrooms
BATHROOMS_ATTRIBUTE = 'aria_label'
BATHROOMS_ATTRIBUTE_VALUE = 'bagni'

## Scrape the floor 
FLOOR_ATTRIBUTE = 'aria-label'
FLOOR_ATTRIBUTE_VALUE = 'piano'
