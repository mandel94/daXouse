'''Global configuration for xpath and css selectors'''

# Scrapy selectors
IMMOBILIARE_SELECTORS = {'XPATH_ONSALE_LIST' : '//ul[@data-cy="result-list"]/li[contains(@class, "in-realEstateResults__item")]',
                         'XPATH_PRICE' : '//li[contains(@class, "in-realEstateListCard__features--main")]/text()',
                         'XPATH_N_OF_ROOMS' : '//li[@aria-label="locali"]/text()',
                         'XPATH_LIVING_SPACE' : '//li[@aria-label="superficie"]/div/text()',
                         'XPATH_BATHROOMS' : '//li[@aria-label="bagni"]/div/text()',
                         'XPATH_AGENCY' : '//div[@class="in-realEstateListCard__referent"]/img/@alt',
                         'XPATH_TITLE' : '//div[@class="in-realEstateListCard__content"]/a/text()',
                         'XPATH_HREF' : '//div[@class="in-realEstateListCard__content"]/a/@href'}
