'''Testing processor functions.

Processors are functions that we pass to Item Loaders' definition and apply 
transformations to data fields as their are selected (through css or xpath 
selection). Selected inputs are passes to input processors, while result of
input processing are passed to output processor. The result of the output 
processor will be finally loaded into the Item.
 
'''
import pytest
import re
from utils.processors import remove_currency_symbols, convert_price_to_int


@pytest.fixture(scope='class', params=['€ 495.000', '595.000 €', '€ 547.000'])
def price(request):
    ''''''
    yield request.param

@pytest.fixture(scope='class', params=['495.000', '495,000', '495_000', 
                                      '495,000.0'])
def price_to_convert(request):
    ''''''
    yield request.param

class TestStringProcessors:
    ''''''
    
    def test_remove_currency_symbols(self, price):
        ''''''
        currencies = ['€', r'/$', '£']
        out = remove_currency_symbols(price)
        no_currency_found=True
        for c in currencies:
            if re.search(c, out):
                '''Search for `c` in `out`'''
                no_currency_found = False
                break
        assert no_currency_found, f'Special symbols found in price: {price}'
    
    def test_convert_price_to_int(self, price_to_convert):
        ''''''
        try:
            convert_price_to_int(price_to_convert)
        except Exception as exc:
            assert False, f'`convert_price_to_int` raised an exection: {exc}' 
        
        

    

    


