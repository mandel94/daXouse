## Todos
- [ ] [scraping-group-of-houses](####scraping-group-of-houses)


# Developers' Documentation

## Scraping Module

### Relevant Files

#### Utilities
+ hauscrape/utils/**/selectors.py
  It containts selectors used by the scraping module, including HTML attributes 
  used by selectors.
+ hauscrape/utils/**/constants.py
  Constants are placed in this unique file.
  

### Spiders
- **onSaleSpider**: Spider for a on-sale page of a particular real estate website. It 
returns the list of homes on-sale on a particular website.  

### Spider Contracts 
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

### Pagination
[Look at some pagination methods here](https://scrapeops.io/python-scrapy-playbook/scrapy-pagination-guide/)
Our approach to pagination involves searching for the *next* button on the 
scraped url, and following the response to parse the next page. 

```python
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

### Items
Items to be loaded must be defined. In Scrapy, the following items are supported:
+ dictionaries
  Convenient and familiar
+ Item objects
  dict-like plus additional features
+ dataclass objects
  Class with fields pre-defined and exported by default (even if no value is 
  found)
+ attrs objects
  Dataclass-like, it requires [attrs package](https://www.attrs.org/en/stable/index.html)  

`hauscrape` formats items as dataclasses. Here is the list of items (subject to
extensions):
+ Home
  Fields (subject to extension):
  + *id*: str, no-default
    Scraped [here](https://www.immobiliare.it/vendita-case/)
  + *city*: str, no-default
    Scraped [here](https://www.immobiliare.it/vendita-case/)
  + *offered_for*: str, no-default, {'for_sale', 'for_rent'}
    The type of offer.
    Scraped [here](https://www.immobiliare.it/vendita-case/)
  + *n_of_rooms*: int, no-default
    How many rooms are in the place?
    Scraped [here](https://www.immobiliare.it/vendita-case/)
  + *District*: str, no-default
    Scraped [here (with example url parameters)](https://www.immobiliare.it/vendita-case/milano/?criterio=rilevanza)
  + *Sub-district*: str, no-default
    Scraped [here (with example url parameters)](https://www.immobiliare.it/vendita-case/milano/?criterio=rilevanza)
  + *Address*: str, no-default
    Scraped [here (with example url parameters)](https://www.immobiliare.it/vendita-case/milano/?criterio=rilevanza)
  + *Active*: bool, no-default
    Is the listing still active?
  + *enter_date*: timestamp
    When the home was first active
  + *exit_date*: timestamp
    When the home turned inactive


  
        
Dataclasses are defined in the items files: 
+ [immobiliare](../hauscrape/utils/immobiliare/items.py) module.

#### Items Loading
##### Item Validation
For an item to be included, validation functions must return `True`
Here is the list of validation functions, grouped by Items:
+ House Item:
  + `is_not_range(Item)` 
    If Item price is a range, the Item is not an actual House, rather a group 
    of houses. In this case, a [methodology](##scraping-group-of-houses) for 
    scraping data on each single house must be implemented.  

#### Scraping Group of Houses
Immobiliare.it can list groups of properties instead of single houses. Scraping 
data on each single house is achieved in the following way: 
+ Check if Item is actually a group of Items: `is_not_range(Item)`
+ If `is_not_range(Item)` returns `True`... [[todo]](##Todos)
+ etc... [[todo]](##Todos)
 
 
### Feed Exports
Loaded Items must be serialized and stored. This is done by generating "export 
feeds". 
[Click here for Scrapy documentation on Feed Exports](https://docs.scrapy.org/en/latest/topics/feed-exports.html)


## Storing Module

## Data Format
Ideally, we would be able to track houses with daily routines. However, we need 
to find a way to efficiently store. 


### JSON Lines
JSON Lines is a convenient format for storing structured data that may be 
processed one record at a time. 