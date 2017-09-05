# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import time
import MySQLdb
import settings
import redis

class FangspiderPipeline(object):
    def process_item(self, item, spider):
        r = redis.StrictRedis(host='192.168.1.106', port=6379, db=0)
        r.set(item['UUID'].encode('utf8'),item['LouPanUrl'].encode('utf8'))
        return item
