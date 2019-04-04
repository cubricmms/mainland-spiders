# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

def compact(s):
    return s if s else None

def strip(s):
    return s.strip('\t').strip('\n').strip('\xa0')

class CityItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()

class LoupanItem(scrapy.Item):
    city = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
    locations = scrapy.Field(input_processor=MapCompose(strip, compact))
    room = scrapy.Field()
    tags = scrapy.Field()
    avg_price = scrapy.Field(input_processor=MapCompose(strip))
    total_price = scrapy.Field(input_processor=MapCompose(strip))

class FangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
