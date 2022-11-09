'''Parsing functions'''

def parse_house_page(self, response, loader):
    '''Parse page of single house item'''
    loader.add_value('test', 'OK')  
    return loader.load_item()