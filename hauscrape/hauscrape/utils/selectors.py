'''Global configuration for xpath and css selectors'''

# Scrapy selectors
IMMOBILIARE_SELECTORS = {'XPATH_ONSALE_LIST' : '@',
                         'XPATH_PRICE' : '//li[@class="in-feat__item--main"]/text()',
                         'XPATH_N_OF_ROOMS' : '//li[@aria-label="locali"]/text()',
                         'XPATH_LIVING_SPACE' : '//li[@aria-label="superficie"]/div/text()',
                         'XPATH_BATHROOMS' : '//li[@aria-label="bagni"]/div/text()',
                         'XPATH_AGENCY' : '//div[@class="in-realEstateListCard__referent"]/img/@alt',
                         'XPATH_TITLE' : '//div[@class="in-realEstateListCard__content"]/a/text()',
                         'XPATH_HREF' : '//div[@class="in-realEstateListCard__content"]/a/@href'}
