import os

from ...utils.immobiliare import constants
from ...utils.immobiliare import selectors

import scrapy

class OnSaleSpider(scrapy.Spider):
    """Spider for immobiliare.com on-sale page

    A spider used for scraping on-sale page. This spider will parse linked
    requests. The initial request will give home listing for sale. Homes from 
    will be parsed in the order provided by the combination of ordering criteria
    (`criterio` parameter + `ordine` parameter).  

    Properties
    ----------
    city : str
        The city you want to access on-sale for. 
    criterio : {'rilevanza', 'prezzo', 'superficie', 'locali', 'dataModifica'}
        The search criteria for ordering results. Parse will be applied 
        according to resulting order.
    ordine : {'asc', 'desc'}, optional
        Order by 'criterio' in ascending or descending order. If not specified, 
        all results will be parsed.
    top: int , optional
        If provided, parse only `top` results from initial list of home for sale.
        For example, if `criteria` is 'prezzo' and `ordine` is 'asc', the Spider
        will parse only the `top` cheapest homes.        
    """
    name = constants.SPIDER_NAME_IMMOBILIARE_ONSALE
    allowed_domains = constants.ALLOWED_DOMAINS_IMMOBILIARE
    
    def start_requests(self):
        '''Perform initial request
        
        It calls https://www.immobiliare.it/vendita-case/milano/
        
        Examples
        --------
        $ scrapy crawl immobiliare_onsale -a city=milano -a criterio=prezzo

        ''' 
        yield scrapy.Request(f'{constants.BASE_URL_IMMOBILIARE_ONSALE}/{self.city}/?criterio={self.criterio}')
    
    def parse(self, response):
        '''Basic callback method
        
        Returns
        -------
        list(str)
            List of URLs of onsale apartment 
        '''
        # Use path expressions
        result_list = response.xpath(selectors.XPATH_ONSALE_LIST_IMMOBILIARE).getall()
        print(result_list)

    

    