# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    EstateArea = scrapy.Field()     
    LouPanName = scrapy.Field()    
    UnitNum = scrapy.Field()
    RefPrice = scrapy.Field()
    AvePrice = scrapy.Field()
    Mortgage = scrapy.Field()
    HuXing = scrapy.Field()
    LouDong = scrapy.Field()
    Floor = scrapy.Field()
    BuildCate = scrapy.Field()
    Area = scrapy.Field()
    Street = scrapy.Field()
    Position = scrapy.Field()
    Face = scrapy.Field()
    Unit = scrapy.Field()
    LouPanUrl = scrapy.Field()
    CrawlTime = scrapy.Field()
    
