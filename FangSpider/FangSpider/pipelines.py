# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import time
import MySQLdb
import settings

class FangspiderPipeline(object):
    def process_item(self, item, spider):
        

        # conn = MySQLdb.connect(
        #     host=settings.DB_Host,
        #     user=settings.DB_User,
        #     passwd=settings.DB_Pwd,
        #     charset='utf8')
        # cursor = conn.cursor()
        # cursor.execute("""use FangSpider;""")
        # cur = conn.cursor()

        # cur.execute(
        #     "insert into tb_newhouse(EstateArea,LouPanName,HuXing,Face,Region,Loc,Area,UnitPrice,TotalPrice,LoupanUrl,CrawlTime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        #     (item['EstateArea'].encode('utf8'),
        #      item['Name'].encode('utf8'),
        #      item['HuXing'].encode('utf8'),
        #      item['Face'].encode('utf8'),
        #      item['Region'].encode('utf8'),
        #      item['Loc'].encode('utf8'),
        #      item['Area'].encode('utf8'),
        #      item['UnitPrice'].encode('utf8'),
        #      item['TotalPrice'].encode('utf8'),
        #      item['LoupanUrl'].encode('utf8'),
        #      item['CrawlTime'].encode('utf8')))
        # cur.close()
        # conn.commit()
        # conn.close()
        return item
