# -*- coding: utf-8 -*-

# Scrapy settings for ke project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
# https://docs.scrapy.org/en/latest/topics/settings.html
# https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import logging

BOT_NAME = "kebot"
ROBOTSTXT_OBEY = False

SPIDER_MODULES = ["ke.spiders"]
NEWSPIDER_MODULE = "ke.spiders"

# log
LOG_LEVEL = logging.DEBUG


USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1",
]

# Maximum number of concurrent items (per response) to process in parallel in item pipelines. (default: 100)
# CONCURRENT_ITEMS = 100

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# The maximum number of concurrent (i.e. simultaneous) requests
# that will be performed by the Scrapy downloader.(default: 8)
# CONCURRENT_REQUESTS_PER_DOMAIN = 8

# The maximum number of concurrent (i.e. simultaneous) requests that will be performed to any single IP. (default: 0)
# If non-zero, the CONCURRENT_REQUESTS_PER_DOMAIN setting is ignored, and this one is used instead.
# In other words, concurrency limits will be applied per IP, not per domain.
# CONCURRENT_REQUESTS_PER_IP = 0

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25  # 250 ms of delay

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    "ke.middlewares.ValidateJsonResponseMiddleware": 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware": 400,
    "scrapy_fake_useragent.middleware.RetryUserAgentMiddleware": 401,
}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    "ke.extensions.SentryLogging": -1,  # Load SentryLogging extension before others
}


# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "ke.pipelines.SaveHousesPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = '.httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


FAKEUSERAGENT_PROVIDERS = [
    # this is the first provider we'll try
    "scrapy_fake_useragent.providers.FakeUserAgentProvider",
    # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    "scrapy_fake_useragent.providers.FakerProvider",
    # fall back to USER_AGENT value
    "scrapy_fake_useragent.providers.FixedUserAgentProvider",
]
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1"
