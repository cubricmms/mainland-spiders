# -*- coding: utf-8 -*-

from os import environ

from scrapy.exceptions import NotConfigured

# Send exceptions to Sentry
SENTRY_DSN = environ.get(
    "SENTRY_DSN",
)
if not SENTRY_DSN:
    raise NotConfigured
