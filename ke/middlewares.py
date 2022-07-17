# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from logging import getLogger

logger = getLogger("ke.middlewares")


class ValidateJsonResponseMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.
        if response.status != 200:
            logger.error("Connect failed, response status %s", response.status)

        if not response.json().get("data"):
            logger.error("Unexpected response %s", response.json())

        # Should return None or raise an exception.
        logger.debug("Validated as normal JSON response.")
        return None
