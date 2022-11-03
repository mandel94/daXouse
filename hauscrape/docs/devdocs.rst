# This is a documentation for developers

## Spiders
- **onSaleSpider**: Spider for a on-sale page of a particular real estate website. It 
returns the list of homes on-sale on a particular website.  

## Spider Contracts 
We test spiders using contracts, which work by defining mock url to request, and
are defined inline inside the docstring of the spiders' parsing methods. 
Contract checking involves parsing the request and later checking if returned 
items or responses satisfy some pre-defined agreement.  
Agreements can be reached on built-in aspects, such as the number of items or 
requests returned by the spider's parsing method. Alternatively, on can define
custom constracts where agreement is reached on custom (and more powerful) 
validations. 

- Contracts for **onSaleSpider**:
    - `parse` method:

## Pagination
[Look at some pagination methods here](https://scrapeops.io/python-scrapy-playbook/scrapy-pagination-guide/)
Our approach to pagination involves searching for the *next* button on the 
scraped url, and following the response to parse the next page. 

```
import scrapy
from pagination_demo.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes_button"
    start_urls = ["http://quotes.toscrape.com/"]
    
    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
        
        # go to next page
        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
```


## Items


