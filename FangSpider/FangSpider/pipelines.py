# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class FangspiderPipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d', time.localtime())
        fileName = now + '.txt'
        with open(fileName, 'a') as fp:
            fp.write(item['Name'].encode('utf8')+'\n')
            fp.write(item['HuXing'].encode('utf8') + '\n')
            fp.write(item['Face'].encode('utf8') + '\n')
            fp.write(item['Region'].encode('utf8') + '\n')
            fp.write(item['Loc'].encode('utf8') + '\n')
            fp.write(item['Area'].encode('utf8') + '\n')
            fp.write(item['UnitPrice'].encode('utf8') + '\n')
            fp.write(item['TotalPrice'].encode('utf8') + '\n')
            fp.write(item['LoupanUrl'].encode('utf8') + '\n')
            fp.write(item['CrawlTime'].encode('utf8') + '\n\n\n')
        return item
