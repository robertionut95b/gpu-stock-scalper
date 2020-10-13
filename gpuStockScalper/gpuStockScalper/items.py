# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GpustockscalperItem(scrapy.Item):
    name = scrapy.Field()
    stock = scrapy.Field()
    url = scrapy.Field()
