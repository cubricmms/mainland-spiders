# -*- coding: utf-8 -*-

import sentry_sdk
from ke.config import SENTRY_DSN


class SentryLogging(object):
    """
    Send exceptions and errors to Sentry.
    """

    @classmethod
    def from_crawler(cls, crawler):
        # instantiate the extension object
        ext = cls()
        # instantiate
        sentry_sdk.init(
            dsn=SENTRY_DSN,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=1.0,
        )
        # return the extension object
        return ext
