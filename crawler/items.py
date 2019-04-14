# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    title = scrapy.Field()
    provider = scrapy.Field()
    start_date = scrapy.Field()
    overview = scrapy.Field()
    link_to_course = scrapy.Field()
    cost = scrapy.Field()


