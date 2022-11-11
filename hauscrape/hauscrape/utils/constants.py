# This script stores costants.
# Base URLs of websites, to be combined with parameters provided at runtime.
# Search criteria

ALLOWED_DOMAINS_IMMOBILIARE = ['immobiliare.it']
BASE_URL_IMMOBILIARE = 'https://www.immobiliare.it'
BASE_URL_IMMOBILIARE_ONSALE = BASE_URL_IMMOBILIARE+'/vendita-case'
CRITERI_RICERCA_IMMOBILIARE = {
    'rilevanza', 
    'prezzo', 
    'superficie', 
    'locali', 
    'dataModifica'
}
SPIDER_NAME_IMMOBILIARE_ONSALE = 'immobiliare_onsale'

# Standards
STRING_STANDARDS = {
    ## All lower-case
    'CITY': r'^[a-z]+$',
    ## All lower-case
    'DISTRICT': r'^[a-z]+$',
    ## (Via/Piazza/Piazzale) (Nome via/piazza/piazzale) (...) (Numero) 
    'ADDRESS': r'^(via|piazza|piazzale|strada)\s([a-z]+\s){1,}\d+$'
}
