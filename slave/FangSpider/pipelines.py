# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import time
import pymongo
import settings

class FangspiderPipeline(object):

    def process_item(self, item, spider):
        client = pymongo.MongoClient(host=settings.Mongodb_Host, port=settings.Mongodb_Port)
        db = client.fang
        my_set = db.test_set
        print type(item)
        print type(dict(item))
        print dict(item)
        my_set.insert(dict(item))
        return item
