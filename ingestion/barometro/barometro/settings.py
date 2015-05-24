# -*- coding: utf-8 -*-

# Scrapy settings for barometro project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os

BOT_NAME = 'barometro'

SPIDER_MODULES = ['barometro.spiders']
NEWSPIDER_MODULE = 'barometro.spiders'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ITEM_PIPELINES = {'scrapy.contrib.pipeline.files.FilesPipeline': 1}
FILES_STORE = '../../downloads/'
FILES_EXPIRES = 90  # don't download again in 90 days



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'barometro (+http://www.yourdomain.com)'
