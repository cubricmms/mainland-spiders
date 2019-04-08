# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class FangPipeline(object):
    def __init__(self):
        # TODO: get rid of hard-coded username
        hostname = 'localhost'
        username = "cubric"
        database = "ke"
        self.connection = psycopg2.connect(host=hostname, user=username, dbname=database)

    def process_item(self, item, spider):
        self.cur = self.connection.cursor()
        self.cur.execute("""
            insert into raw_data(city, name, status, locations,
                room, tags, avg_price, total_price) values(%s, %s, %s, %s, %s, %s, %s, %s);""",(
                    item.get('city', 'NA'),
                    item.get('name', 'NA'),
                    item.get('status', 'NA'),
                    item.get('locations', 'NA'),
                    item.get('room', 'NA'),
                    item.get('tags', 'NA'),
                    item.get('avg_price', 'NA'),
                    item.get('total_price', 'NA')
                    )
                )
        self.connection.commit()
        return item
