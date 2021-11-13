# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from pymongo import MongoClient

class AmazonPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(host="localhost", port=27017)
        db = self.conn['Amazon_scrap']

        self.collection = db['amazon_scrap']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
