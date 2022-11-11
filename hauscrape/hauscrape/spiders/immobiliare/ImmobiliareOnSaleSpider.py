import os
from abc import ABC, abstractproperty
import time

from ...utils import constants
from ...utils.immobiliare import immobiliare_selectors 
from ...utils.items import HouseList, House
from ...utils.itemLoaders import HouseLoader
from ..abstract import OnSaleSpider

import scrapy
import pandas as pd
     

class ImmobiliareOnSaleSpider(OnSaleSpider):
    """Spider for immobiliare.com on-sale page.

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
    name = constants.SPIDER_NAMEONSALE
    allowed_domains = constants.ALLOWED_DOMAINS

    @property
    def base_url(self):
        return f"{constants.BASE_URLONSALE}"

    @property
    def xpath_onsale_list(self):
        return f"{immobiliare_selectors.XPATH_ONSALE_LIST}"

    def __init__(self, city: str, criterio: str, *args, **kwargs):
        super().__init__(city, criterio, *args, **kwargs)
        print(f"Initialize OnSaleSpider w/ params [city={self.city}, "
              f"criterio={self.criterio}]")

    def start_requests(self):
        '''Perform initial request
        
        It calls https://www.immobiliare.it/vendita-case/milano/
        
        Examples
        --------
        $ scrapy crawl immobiliare_onsale -a city=milano -a criterio=prezzo

        ''' 
        # https://stackoverflow.com/questions/44922961/scrapy-multiple-requests-and-fill-single-item
        yield scrapy.Request(f'{self.base_url}/{self.city}/?criterio={self.criterio}', 
                             callback=self.parse_onsale_list)
        # Check if there is a 'Next' page

    
    def parse_house_page(self, response):
        '''Parse page of single house item'''
        self.logging.debug("Parsing house page item")
        HouseItemLoader = HouseLoader(item=House(), response=response)
        for k,v in response.meta.items():
            HouseItemLoader.add_value(k, v)
        # Finish loading House Item
        # HouseItemLoader.add_value('test', 'test')
        yield HouseItemLoader.load_item()


    def parse_onsale_list(self, response):
        '''Basic callback method
        
        Returns
        -------
        list(str)
            List of URLs of onsale apartment 
        '''
    
        houseListItem = HouseList()
        # Last update timestamp
        houseListItem['timestamp'] = time.time()
        # Use path expressions to get list of houses.
        # Result will be a list of Selectors
        house_list = response.xpath(self.xpath_onsale_list)
        # For each house Selector
        for house in house_list:
            # Start collecting values to load on Item
            data=dict()
            data['city'] = self.city
            data['offered_for'] = 'for_sale'
            data['title'] = house.xpath(immobiliare_selectors.XPATH_TITLE).get()
            data['price'] = int(house.xpath(immobiliare_selectors.XPATH_PRICE).get())
            data['n_of_rooms'] = house.xpath(immobiliare_selectors.XPATH_N_OF_ROOMS).get()
            data['living_space'] = house.xpath(immobiliare_selectors.XPATH_LIVING_SPACE).get()
            data['bathrooms'] = house.xpath(immobiliare_selectors.XPATH_BATHROOMS).get()
            data['agency'] = house.xpath(immobiliare_selectors.XPATH_AGENCY).get()
            # Get href for following request
            href = house.xpath(immobiliare_selectors.XPATH_HREF).get()
            # Request house-specific url to end values collection
            yield scrapy.Request(href, 
                                 callback=parse_house_page, 
                                 meta=data)

    




    

    