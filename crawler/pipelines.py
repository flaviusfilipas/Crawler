# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class CrawlerPipeline(object):

    def __init__(self):
        self.connection = pymongo.MongoClient('localhost', 27017)
        db = self.connection['licenta-db']
        self.collection = db['course']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
