# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project = scrapy.Field()
    id = scrapy.Field()
    type = scrapy.Field() # (flat, house)
    price = scrapy.Field()
    rooms = scrapy.Field()
    area = scrapy.Field()
    availability = scrapy.Field()
