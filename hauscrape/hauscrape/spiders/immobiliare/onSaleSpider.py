from unicodedata import name
import scrapy

class OnSaleSpider(scrapy.Spider):
    """ Spider for immobiliare.com on-sale page

    A spider used for scraping on-sale page. This spider will parse linked
    requests. The initial request will give home listing for sale. Homes from 
    will be parsed in the order provided by the combination of ordering criteria
    (`criterio` parameter + `ordine` parameter).  
    
    :attribute:: name
    :attribute:: allowed_domains
    :method:: 

    Parameters
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

    Methods
    -------
    start_requests()
        Perform initial request 
    parse()
        Basic callback method
    """
    name = 'immobiliare_onsale'
    allowed_domains = ['immobiliare.it']
    
    def start_requests(self):
        yield scrapy.Request(f'https://www.immobiliare.it/vendita-case/{self.city}/?criterio={self.criterio}')
    
    def parse(self, response):
        print(self.criterio)
        print('OK')