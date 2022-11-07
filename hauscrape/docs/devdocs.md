## Todos
- [ ] [scraping-group-of-houses](###scraping-group-of-houses)
- [ ] [define-collection-checks](##collection-runtime-checks)

# Scraping Module

## Relevant Files

### Utilities
+ hauscrape/utils/**/selectors.py
  It containts selectors used by the scraping module, including HTML attributes 
  used by selectors.
+ hauscrape/utils/**/constants.py
  Constants are placed in this unique file.
+ hauscrape/utils/**/customClasses.py 
  
## Spiders
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

### Selectors
`hauscrape` uses the [Xpath](https://www.w3.org/TR/xpath/all/) language for 
scraping XML documents. 
Selectors are defined in the *selectors.py* file for each website 
(hauscrape/utils/**/selectors.py, where ** is the real estate platform).

*selectors.py* files define string constants, with each constant being the Xpath
pattern to one particular node in the page to be scraped. Nodes are the ultimate 
data to be scraped, that is, the values that will be assigned to the the 
features defined in [Items](##items). 

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

## Items
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

**`hauscrape` formats items as dataclasses**. Here is the list of items (subject to
extensions):
+ Home
  Fields (subject to extension):
  + *id*: str, no-default  
  + *city*: str, no-default  
  + *offered_for*: str, no-default, {'for_sale', 'for_rent'}  
    The type of offer.  
  + *n_of_rooms*: int, no-default  
    How many rooms are in the place?
  + *living_space(m^2)*: int, no-default 
    Living space of an apartment.
    Scraped 
  + *district*: str, no-default  
  + *sub_district*: str, no-default  
  + *address*: str, no-default  
  + *active*: bool, no-default
    Is the listing still active?
  + *entry_date*: timestamp
    When the home was first active
  + *exit_date*: timestamp
    When the home turned inactive
  + *agency*: str, optional, default=`None`  
    Agency, if any, that posted the listing


Dataclasses are defined in the items files: 
+ [immobiliare](../hauscrape/utils/items.py) module.

### Items Loaders
As per stated in Scrapy's docs, items provide the container of scraped data,
while Item Loaders provide the mechanism for populating that container.
Item Loader is a class, so an instance of it must be instantiated. Values are 
then collected inside the Item Loader using [Selectors](###selectors). 

Input and Output processing functions are defined in the [`processors.py`](../hauscrape/utils/processors.py) file

Given that we use dataclass items, that require all field to be passed, but Item
Loaders add values incrementally, we might need to difine items using the 
field()` function with a default argument.  

Fields that require processor functions are:
  + *id*, needs all the intrinsic properties of the house to be first selected 
    with different selectors. The various selections are combined and digested 
    using an hash function to generate the output id.
  


#### Item Validation
For an item to be included, validation functions must return `True`
Here is the list of validation functions, grouped by Items:
+ House Item:
  + `is_price_not_range(Item)` 
    If Item price is a range, the Item is not an actual House, rather a group 
    of houses. In this case, a [methodology](##scraping-group-of-houses) for 
    scraping data on each single house must be implemented.  

### Scraping Group of Houses
Immobiliare.it can list groups of properties instead of single houses. Scraping 
data on each single house is achieved in the following way: 
+ Check if Item is actually a group of Items: `is_not_range(Item)`
+ If `is_price_not_range(Item)` returns `True`... [[todo]](##Todos)
+ etc... [[todo]](##Todos)
 

## Feed Exports
Loaded Items must be serialized and stored. This is done by generating "export 
feeds". 
[Click here for Scrapy documentation on Feed Exports](https://docs.scrapy.org/en/latest/topics/feed-exports.html)


# Storage Module

## Storage Solution
**What** that needs to be persisted:

**Where** do we persist the data? 


## Data Format
Ideally, we would be able to track houses with daily routines. However, we need 
to find a way to efficiently store data on prices. Data on house, and prices 
in particular, can change over time. Thus we need to find a way to efficiently
update the database. In order to do that, we must set periodic routines to be 
run at regular time intervals. At each run, the program collects data on all 
listed homes, from all the data sources. The data is subject to some 
[checks](##collection-runtime-checks) during this periodic routines.
If those checks all return `True`, the data will finally update the database. 
Else, it means that nothing changed and the data will not update the database.


## Collection-runtime Checks 
Periodically [[conf-parameters]](###configuration-parameters), data collection
routine is triggered. During collection, some checks are perfomed on each data
point, in order to establish if that data point has changed with respect to its
previous stored version, or if that data point is new and should be added to the 
database.  
The following checks are performed:  
+ Check 1:
  check if the house id is already in the database. House ids are
  obtained directly from the data (or some processing of it), in order to crearly 
  establish that an Item is exactly the same as the one collected in a previous
  run. This is kind of difficult to perform, given that different websites might 
  list the same house under different ids. For an house to be identified with the
  same id, independently from the data source, we must implement an `idFactory`,
  that use the same type of information on a house to produce an id that is the 
  same across all data sources. Check [idFactory](###idfactory) to know more.  

+ Check 2: 


JSON Lines is a convenient format for storing structured data that may be 
processed one record at a time. 

# Configuration File

## Configuration Parameters
+ **DATA_COLLECTION_PERIODICITY**: datetime.timedelta.  
  A duration expressing the difference between two date, time, or datetime 
  instances to microsecond resolution. 


# Custom Classes
Custom classes are defined in [customClasses.py](../hauscrape/utils/customClasses.py)
Here is the list of custom classes used by `hauscrape`:
+ ...

# Utilities Functions

## digest_id
House ids are obtained directly from the data (or some processing of it), 
in order to crearly establish that an Item is exactly the same as the one 
collected in a previous run. This is kind of difficult to perform, given that
different websites might list the same house under different ids. For an house 
to be identified with the same id, independently from the data source, we must 
implement an `idFactory`, that use the same type of information on a house to 
produce an id that is the same across all data sources.   
The data used to produce the id are intrinsic properties of an house, that 
unambiguously identify it. These intrinsic properties are the following:
  + *city*
  + *district* 
  + *sub_district*
  + *address*
  + *number_of_rooms* 
  + *living_space(m^2)*
  + *floor*
  + *agency*
  + other data that helps discriminating house listings

`digest_id` works by hashing the intrinsic properties of an house listing:
the resulting digest will be the identifier (*id*) of the listing, used for 
identifing it across all supported real estate platforms.

For each house listing:
  + `digest_id` returns an `id` for the house;
  + if `id` is not in the database, add it to the database;
  + if `id` is already in the database, do nothing, and pass to the following 
    house listing.

`digest_id` is part of the transformation process applied while scraping the 
data.

The intrinsic properties that are used for digesting the identifier must satisfy
some specifications, whose presence is checked during Item Loading. We shall 
thus specify a standard for the intrinsic properties of an house, that should 
be valid throughout the websites hauscrape gets the data from. Indeed, we must
be sure that:
  + the same intrinsic properties can be obtained from all the websites;
  + intinsic properties are processed during Item Loading in such a way that the 
    processing output respects clearly specified formatting constraints. 
    Hashing a property implies that each small change in the hash function input
    results in a completely different digest, hence identifier. 

Let's specify here the standard for each of the intrinsic properties:  
  + *city*: lower-case string, without whitespaces.
  + *district*: lower-case string, without whitespaces.
  + *sub_district*: 
  + *address*
  + *number_of_rooms* 
  + *filter_intrinsic_prop*
  + *floor*
  + *agency*
  + other data that helps discriminating house listings

One way to implement this standard is to provide an interface for the intrinsic
properties that is valid independently from how that property is formatted in 
a particular website. This interface is a dictionary, whose keys are the 
intrinsic properties as their are found in the different data sources/websites.
The values of the interface are the intrinsic properties that will be used by 
hauscrape. Those value will reconcile the different formats in which we can find
the same information to a common representation standard of that information. 
Instad of using a chain of transformation for reconciling the string formats, 
we manually map the set of different formats to the sub-set of standard formats.
Applying a chain of transformation introduces a computional risk, that can 
result in a final value that is different from the standard one. The interface 
approach eliminates this risk altogether, applying the mapping from scraped
values to standard values in a constrained way.

## Parallel Computing
Here is a list of tasks which can be divided into parallel sub-task for 
improving performance:
+ [`digest_id`](##digest_id)

