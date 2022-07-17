# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

from scrapy.exceptions import DropItem
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from .models import HouseInfoModel, create_table, db_connect


class SaveHousesPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.db_session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.db_session()
        house_info = HouseInfoModel()

        house_info.community_name = item["community_name"]
        house_info.url = item["url"]
        house_info.square_meter = item["square_meter"]
        house_info.avg_square_meter = item["avg_square_meter"]
        house_info.total = item["total"]
        house_info.floor_plan = item["floor_plan"]
        house_info.type = item["type"]
        house_info.direction = item["direction"]

        # check whether the house_info exists
        now = datetime.today()
        exists = (
            session.query(HouseInfoModel)
            .filter(
                and_(
                    HouseInfoModel.url == house_info.url,
                    HouseInfoModel.created_time > now,
                )
            )
            .first()
            is not None
        )

        try:
            if not exists:
                session.add(house_info)
                session.commit()
        except Exception:
            session.rollback()
            raise DropItem()
        finally:
            session.close()

        return item
