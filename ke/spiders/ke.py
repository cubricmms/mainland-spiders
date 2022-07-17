# -*- coding: utf-8 -*-

from math import ceil

import scrapy
from scrapy.spiders import CrawlSpider
from tqdm import tqdm

from ..items import HouseInfoItem

HOUSE_LIST_API = "https://map.ke.com/proxyApi/i.c-pc-webapi.ke.com/map/houselist"


class KeSpider(CrawlSpider):
    name = "ke"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_code = 310000  # Shanghai
        self.page_size = 10  # default
        self.current_page = 1

    def construct_query_data(self, current_page=1):
        return {
            "cityId": str(self.city_code),
            "dataSource": "ESF",
            "curPage": str(current_page),
            "condition": "",
            "type": "",
            "resblockId": "",
            "maxLatitude": "31.555649742924622",
            "minLatitude": "30.913909912780674",
            "maxLongitude": "121.63306517041237",
            "minLongitude": "120.91729534006193",
        }

    def start_requests(self):
        yield scrapy.FormRequest(
            url=HOUSE_LIST_API,
            method="GET",
            formdata=self.construct_query_data(),
            callback=self.parse_item,
        )

    def parse_item(self, response):
        _root = response.json().get("data")
        # Parse the data from first response
        house_list = _root.get("list")
        for item in house_list:
            house_info_item = HouseInfoItem()
            try:
                _ = item.get("desc").split("/")
                house_info_item["floor_plan"] = _[0]
                house_info_item["square_meter"] = _[1]
                house_info_item["direction"] = _[2]
                house_info_item["community_name"] = _[3]
                house_info_item["type"] = item.get("cardType")
                house_info_item["url"], _ = (
                    item.get("actionUrl").split("?")
                    if item.get("actionUrl")
                    else (None, None)
                )
                house_info_item["avg_square_meter"] = item.get("unitPriceStr").rstrip(
                    "元/平"
                )
                house_info_item["total"] = item.get("priceStr")
                house_info_item["square_meter"] = house_info_item[
                    "square_meter"
                ].rstrip("㎡")
                house_info_item["direction"] = "".join(
                    sorted(house_info_item["direction"])
                ).strip()

            except IndexError as e:
                self.logger.exception("Item desc has undealt case: %s", e)

            yield house_info_item

        # take care the rest of pages
        self.current_page = _root.get("page")
        self.total_pages = _root.get("total")
        self.progress_bar = tqdm(total=ceil(self.total_pages // self.page_size))

        # for i in tqdm(range(numbers_of_operation)):
        #     self.current_page += 1
        #     yield scrapy.FormRequest(
        #         url=HOUSE_LIST_API,
        #         method="GET",
        #         formdata=self.construct_query_data(),
        #         callback=self.parse_page,
        #     )
