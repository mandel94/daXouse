'''Abstract classes are defined here'''

from abc import ABC, abstractproperty
import scrapy

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

    @abstractproperty
    def xpath_title(self):
        '''Xpath selector of the house title'''
        pass

    @abstractproperty
    def xpath_price(self):
        '''Xpath selector of the house price'''
        pass

    @abstractproperty
    def xpath_rooms(self):
        '''Xpath selector for the number of rooms'''
        pass


    @abstractproperty
    def xpath_living_space(self):
        '''Xpath selector of the house living space'''
        pass


    @abstractproperty
    def xpath_bathrooms(self):
        '''Xpath selector of the number of bathrooms'''
        pass


    @abstractproperty
    def xpath_floor(self):
        '''Xpath selector of the house floor'''
        pass


    @abstractproperty
    def xpath_is_luxury(self):
        '''Xpath for checking if it is a luxury house'''
        pass
