# -*- coding: utf-8 -*-
import scrapy
import re
import time
import uuid
from FangSpider.items import FangspiderItem


class NewfangspiderSpider(scrapy.Spider):
    name = 'NewFangSpider'
    allowed_domains = ['fang.com']
    start_urls = [
        'http://newhouse.fang.com/house/s/c9y/',
        'http://newhouse.sh.fang.com/house/s/c9y/',
        'http://newhouse.gz.fang.com/house/s/c9y/',
        'http://newhouse.sz.fang.com/house/s/c9y/',
        'http://newhouse.dg.fang.com/house/s/c9y/',
        'http://newhouse.huizhou.fang.com/house/s/c9y/',
        'http://newhouse.fs.fang.com/house/s/c9y/',
        'http://newhouse.zs.fang.com/house/s/c9y/',
        'http://newhouse.zh.fang.com/house/s/c9y/',
        'http://newhouse.hz.fang.com/house/s/c9y/',
        'http://newhouse.tj.fang.com/house/s/c9y/']

    def parse(self, response):
        try:
            # print 'response.url:' + response.url
            loupanlist = response.xpath('//div[@class="contentList fl clearfix"]/ul[@class="flist"]')
            for i in xrange(1, len(loupanlist)):
                loupanurl = loupanlist[i - 1].xpath('./li[1]/div[@class="finfo c_333_f14"]/h3/a/@href').extract()[0]
                # print 'loupanurl:',loupanurl
                yield scrapy.Request(loupanurl, callback=self.parseLoupanInfo)
            baseurl = re.findall(re.compile(r'.*?com'), response.url)[0]
            if response.xpath('//div[@class="contentList fl clearfix"]/div[@id="sjina_D25_101"]/ul[@class="clearfix"]/li[@class="fr"]/a[@class="next"]/@href').extract() != []:
                nextpageurl = baseurl + response.xpath('//div[@class="contentList fl clearfix"]/div[@id="sjina_D25_101"]/ul[@class="clearfix"]/li[@class="fr"]/a[@class="next"]/@href').extract()[0]
                # print 'nextpageurl:' + nextpageurl
                yield scrapy.Request(nextpageurl, callback=self.parse)
        except Exception as e:
            print e

    def parseLoupanInfo(self,response):
            items = FangspiderItem()
            items['UUID'] = str(uuid.uuid1())
            items['LouPanUrl'] = response.url
            yield items 





