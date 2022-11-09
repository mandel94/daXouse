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