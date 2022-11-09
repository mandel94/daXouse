# Project settings module
SPIDER_MODULES = ['hauscrape.spiders']

ITEM_PIPELINES = {
    'hauscrape.utils.pipelines.HousePipeline': 100
}