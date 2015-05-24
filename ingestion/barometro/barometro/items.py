# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BarometroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AvanceItem(scrapy.Item):
    barometro_id = scrapy.Field()
    month = scrapy.Field()
    year = scrapy.Field()
    download_link = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
