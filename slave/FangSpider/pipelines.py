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
        

        conn = MySQLdb.connect(
            host=settings.DB_Host,
            user=settings.DB_User,
            passwd=settings.DB_Pwd,
            charset='utf8')
        cursor = conn.cursor()
        cursor.execute("""use FangSpider;""")
        cur = conn.cursor()

        cur.execute(
            "insert into tb_fanghouse(EstateArea,LouPanName,UnitNum,RefPrice,AvePrice,Mortgage,HuXing,LouDong,Floor,BuildCate,Area,Street,Position,Face,Unit,LouPanUrl,CrawlTime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (item['EstateArea'].encode('utf8'),
             item['LouPanName'].encode('utf8'),
             item['UnitNum'].encode('utf8'),
             item['RefPrice'].encode('utf8'),
             item['AvePrice'].encode('utf8'),
             item['Mortgage'].encode('utf8'),
             item['HuXing'].encode('utf8'),
             item['LouDong'].encode('utf8'),
             item['Floor'].encode('utf8'),
             item['BuildCate'].encode('utf8'),
             item['Area'].encode('utf8'),
             item['Street'].encode('utf8'),
             item['Position'].encode('utf8'),
             item['Face'].encode('utf8'),
             item['Unit'].encode('utf8'),
             item['LouPanUrl'].encode('utf8'),
             item['CrawlTime'].encode('utf8')
             ))
        cur.close()
        conn.commit()
        conn.close()
        return item
