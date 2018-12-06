# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import pymongo
from scrapy.conf import settings


class KePipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
                settings['MONGDB_SERVER'],
                settings['MONGODB_PORT']
                )
        db = connection[settings['MONGODB_DB']]
        now = time.strftime("%x")
        self.collection = db['_'.join([settings['MONGODB_COLLECTION'],now])]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
