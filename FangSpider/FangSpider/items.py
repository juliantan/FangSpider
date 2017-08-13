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
    Name = scrapy.Field()
    HuXing = scrapy.Field()
    Face = scrapy.Field()
    Region = scrapy.Field()
    Loc = scrapy.Field()
    Area = scrapy.Field()
    UnitPrice = scrapy.Field()
    TotalPrice = scrapy.Field()
    LoupanUrl = scrapy.Field()
    CrawlTime = scrapy.Field()
    
