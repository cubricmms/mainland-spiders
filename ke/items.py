# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class HouseInfoItem(Item):
    floor_plan = Field()
    square_meter = Field()
    direction = Field()
    community_name = Field()
    type = Field()
    url = Field()
    avg_square_meter = Field()
    total = Field()
