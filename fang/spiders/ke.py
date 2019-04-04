# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import Request
from fang.items import CityItem, LoupanItem
from urllib.parse import urljoin
from urllib.parse import urlparse

class KeSpider(scrapy.Spider):
    name = 'ke'
    allowed_domains = ['ke.com']
    start_urls = ['https://www.ke.com/city/']
    def parse(self, response):
        url_scheme = 'https:'
        members = response.css("div.city-item .city_list .CLICKDATA")
        for member in members:
            yield Request(urljoin(url_scheme, member.css("a::attr(href)").extract_first()+ "/loupan"),
                    callback=self.parse_city)

    def parse_city(self, response):
        if "0" == response.css("div.resblock-have-find span.value::text").extract_first():
            return


        parsed_uri = urlparse(response.url)
        base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        next_url = ""
        if not "pg" in response.url:
            next_url = urljoin(base_url, "loupan/pg2")
        else:
            current_page = response.url.split("pg")[1]
            next_page = int(current_page) + 1
            next_url = urljoin(base_url, "loupan/pg"+str(next_page))

        root = response.css("div.resblock-desc-wrapper")
        for member in root:
            l = ItemLoader(item=LoupanItem(), selector=member)
            city = response.css("a.s-city::text").extract_first()
            l.add_value("city", city)
            l.add_css("name", "div.resblock-name a::text")
            l.add_css("status", "div.resblock-name span::text")
            l.add_css("locations", "a.resblock-location::text")
            l.add_css("room", "a.resblock-room span::text")
            l.add_css("tags", "div.resblock-tag span::text")
            l.add_css("avg_price", "div.resblock-price div.main-price span::text")
            l.add_css("total_price", "div.resblock-price div.second::text")
            yield l.load_item()
        yield Request(next_url, callback=self.parse_city)
