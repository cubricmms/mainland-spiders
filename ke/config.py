# -*- coding: utf-8 -*-

from dotenv import dotenv_values
from scrapy.exceptions import NotConfigured

config = dotenv_values(".env")

# Send exceptions to Sentry
SENTRY_DSN = config.get("SENTRY_DSN")
if not SENTRY_DSN:
    raise NotConfigured("Sentry not configured")

DB_USER = config.get("DB_USER")
DB_PASSWORD = config.get("DB_PASSWORD")
if not DB_USER or not DB_PASSWORD:
    raise NotConfigured

DB_CONNECTION = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}".format(
    drivername="postgresql+psycopg2",
    user=DB_USER,
    passwd=DB_PASSWORD,
    host="localhost",
    port="5432",
    db_name="sh_estates",
)
