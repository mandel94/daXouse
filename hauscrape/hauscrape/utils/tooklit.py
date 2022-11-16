from scrapy import Selector

# ***PENDING DELETION***
# def is_group(house: Selector):
#     '''Check if house is actually a group of houses'''
#     # Check if there is div referred to price range (for a group of houses there
#     # is no puntual price, rather a range)
#     rangePriceDiv = house\
#           .xpath('//div[@class="in-realEstateListCard__features--range"]')\
#           .get() 
#     if rangePriceDiv:
#         return True
#     return False
