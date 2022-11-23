import logging
from abc import ABC
import asyncio
import json

import pandas as pd
import scrapy
from scrapy import Selector, Request
from scrapy.utils.response import open_in_browser
import aiohttp 

from ...utils import constants
from ...utils.itemLoaders import HouseLoader
from ...utils.items import House
from ...utils.selectors import IMMOBILIARE_SELECTORS
from ..abstract import OnSaleSpider


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
        ''''''
        return f"{IMMOBILIARE_SELECTORS['XPATH_ONSALE_LIST']}"

    @property
    def xpath_title(self):
        ''''''
        return f"{IMMOBILIARE_SELECTORS['XPATH_TITLE']}"

    @property
    def xpath_price(self):
        ''''''
        return f"{IMMOBILIARE_SELECTORS['XPATH_PRICE']}"

    @property
    def xpath_rooms(self):
        ''''''
        return f"{IMMOBILIARE_SELECTORS['XPATH_ROOMS']}"

    @property
    def xpath_living_space(self):
        ''''''
        return f"{IMMOBILIARE_SELECTORS['XPATH_LIVING_SPACE']}"

    @property
    def xpath_bathrooms(self):
        ''''''
        return f"{IMMOBILIARE_SELECTORS['XPATH_BATHROOMS']}"

    @property
    def xpath_floor(self):
        ''''''
        return f"{IMMOBILIARE_SELECTORS['XPATH_FLOOR']}"

    @property
    def xpath_is_luxury(self):
        ''''''
        return f"{IMMOBILIARE_SELECTORS['XPATH_IS_LUXURY']}"

    @property
    def xpath_href(self):
        return f"{IMMOBILIARE_SELECTORS['XPATH_HREF']}"

    @property 
    def xpath_additional_data_object(self):
        return f"{IMMOBILIARE_SELECTORS['XPATH_ADDITIONAL_DATA_OBJECT']}"

    def __init__(self, city: str='milano', criterio: str='rilevanza', *args, **kwargs):
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

    async def parse_sub_page(self, href):
        '''Parse the web page of a specific house to get additional data to
           be loaded in the final item.
        '''
        async with aiohttp.ClientSession() as session:
            async with session.get(href) as sub_response:
                additional_data = await sub_response.text()
                # logging.debug(f"ADDITIONAL DATA = {additional_data}")
                return additional_data
    
    def get_additional_data_object(self, selector) -> dict:
        ''' Get dictionary with additional data from individual house pages.

        :param selector: The `~scrapy.Selector` relative to which 
            :attr:`self.xpath_house_page` will be applied.
        :type selector: :class:`~scrapy.Selector` object.
        '''
        # Get raw data
        xpath = self.xpath_additional_data_object
        raw_object = selector.xpath(xpath).get()

        # Parse to python dictionary and return
        return json.loads(raw_object)

    async def parse_onsale_list(self, response):
        '''Basic callback method
        
        Returns
        -------
        list(str)
            List of URLs of onsale apartment 
        '''
        # Last update timestamp
        ## Use path expressions to get list of houses.
        ## Result will be a list of Selectors
        house_list = response.xpath(self.xpath_onsale_list)
        for house in house_list:
            # Create house selector from house text
            house_selector = Selector(text=house.get())

            # Create Item Loader
            house_loader = HouseLoader(House(), selector=house_selector) 
            house_loader.add_value('city', self.city)
            house_loader.add_xpath('price', self.xpath_price)
            house_loader.add_xpath('title', self.xpath_title)
            house_loader.add_xpath('rooms', self.xpath_rooms)
            house_loader.add_xpath('living_space', self.xpath_living_space)
            house_loader.add_xpath('bathrooms', self.xpath_bathrooms)
            house_loader.add_xpath('floor', self.xpath_floor)
            house_loader.add_xpath('is_luxury', self.xpath_is_luxury)

            # Get href for nested Request
            house_href = house.xpath(self.xpath_href).get()
            additional_data_text = asyncio.run(self.parse_sub_page(house_href))
            additional_data_object = self.get_additional_data_object(Selector(text=additional_data_text))
            logging.debug(f"ADDITIONAL DATA OBJECT = {additional_data_object['listing']}")
            # Collect rest of information from nested Request
            break
            
            
            # house_loader.add_xpath
            yield house_loader.load_item()







    

    