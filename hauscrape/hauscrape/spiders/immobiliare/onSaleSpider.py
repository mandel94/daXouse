import os
from abc import ABC, abstractproperty
import time

from ...utils.immobiliare import constants
from ...utils.immobiliare import selectors
from ...utils.items import HouseList, House
from ...utils.itemLoaders import HouseLoader

import scrapy
import pandas as pd


class OnSaleSpider(scrapy.Spider, ABC):
    '''Interface for scraping house listings from real estate websites.
    
    Inherits from Scrapy's Spider.
    
    '''

    def __init__(self, city:str, criterio:str, *args, **kwargs):
        super(OnSaleSpider, self).__init__(*args, **kwargs)
        self.city = city
        self.criterio = criterio

    @abstractproperty
    def base_url(self):
        '''Base URL of the website to scrape'''
        pass

    @abstractproperty
    def xpath_onsale_list(self):
        '''Xpath selector of the house listing'''
        pass
     


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
    name = constants.SPIDER_NAME_IMMOBILIARE_ONSALE
    allowed_domains = constants.ALLOWED_DOMAINS_IMMOBILIARE

    @property
    def base_url(self):
        return f"{constants.BASE_URL_IMMOBILIARE_ONSALE}"

    @property
    def xpath_onsale_list(self):
        return f"{selectors.XPATH_ONSALE_LIST_IMMOBILIARE}"

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
            # Start collecting values for the item
            # Initialize Item Loader

            houseItemLoader = HouseLoader(item=House(), response=house)
            # Get values from this house response
            title = house.xpath(selectors.XPATH_TITLE_IMMOBILIARE).get()
            price = int(house.xpath(selectors.XPATH_PRICE_IMMOBILIARE).get())
            n_of_rooms = house.xpath(selectors.XPATH_N_OF_ROOMS_IMMOBILIARE).get()
            living_space = house.xpath(selectors.XPATH_LIVING_SPACE_IMMOBILIARE).get()
            bathrooms = house.xpath(selectors.XPATH_BATHROOMS_IMMOBILIARE).get()
            agency = house.xpath(selectors.XPATH_AGENCY_IMMOBILIARE).get()
            # Get href for following request
            href = house.xpath(selectors.XPATH_HREF_IMMOBILIARE).get()

            # Get values by requesting the house specific url

            # Load Item
            houseItemLoader.add_value('city', self.city)
            houseItemLoader.add_value('offered_for', 'for_sale')
            
            # Populate the HouseItem

            # Add the house to the houseListItem

        yield house_list

    

    