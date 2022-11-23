'''Global configuration for xpath and css selectors'''

# Scrapy selectors
IMMOBILIARE_SELECTORS = {'XPATH_ONSALE_LIST' : '//ul[@data-cy="result-list"]/li[contains(@class, "in-realEstateResults__item")]',
                         'XPATH_PRICE' : '//li[contains(@class, "in-realEstateListCard__features--main")]/text()',
                         'XPATH_ROOMS' : '//li[@aria-label="locali"]/div/text()',
                         'XPATH_LIVING_SPACE' : '//li[@aria-label="superficie"]/div/text()',
                         'XPATH_BATHROOMS' : '//li[@aria-label="bagni"]/div/text()',
                         'XPATH_AGENCY' : '//div[@class="in-realEstateListCard__referent"]/img/@alt',
                         'XPATH_TITLE' : '//a[@class="in-card__title"]/text()',
                         'XPATH_HREF' : '//a[@class="in-card__title"]/@href',
                         'XPATH_FLOOR': '//li[@aria-label="piano"]/div/text()',
                         'XPATH_IS_LUXURY': '//li[@aria-label="lusso"]',
                         'XPATH_ADDITIONAL_DATA_OBJECT': '//script[@id="js-hydration"]/text()'}


