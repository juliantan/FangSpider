# -*- coding: utf-8 -*-
import scrapy
import re
import time
from FangSpider.items import FangspiderItem
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request

class NewfangspiderSpider(RedisSpider):
    name = 'NewFangSpider'
    allowed_domains = ['fang.com']
    redis_key = "NewFangSpider:start_urls"
    start_urls = ['','sh.','gz.','sz.','dg.','huizhou.','fs.','zs.','zh.','hz.','tj.']

    def start_requests(self):
        for url in self.start_urls:
            url = 'http://newhouse.{0}fang.com/house/s/c9y/'.format(url)
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        try:
            # print 'response.url:' + response.url
            loupanlist = response.xpath(
                '//div[@class="contentList fl clearfix"]/ul[@class="flist"]')
            for i in xrange(1, len(loupanlist)):
                loupanurl = loupanlist[i - 1].xpath('./li[1]/div[@class="finfo c_333_f14"]/h3/a/@href').extract()[0]
                # print 'loupanurl:',loupanurl
                yield scrapy.Request(loupanurl, callback=self.parseLoupanInfo)
            baseurl = re.findall(re.compile(r'.*?com'), response.url)[0]
            nextpage = response.xpath('//div[@class="contentList fl clearfix"]/div[@id="sjina_D25_101"]/ul[@class="clearfix"]/li[@class="fr"]/a[@class="next"]/@href').extract()
            if nextpage != []:
                nextpageurl = baseurl + nextpage[0]
                # print 'nextpageurl:' + nextpageurl
                yield scrapy.Request(nextpageurl, callback=self.parse)
        except Exception as e:
            print e

    def parseLoupanInfo(self, response):
        # print 'response.url:' + response.url
        items = FangspiderItem()
        estateArea = response.xpath('//div[@id="fyxq_B01_03"]/ul[@class="tf f12"]/li[2]/a/text()').extract()
        louPanName = response.xpath('//div[@class="right_box"]/p[@id="fyxq_B01_05"]/a/text()').extract()
        unitNum = response.xpath('//div[@class="right_box"]/p[@id="fyxq_B01_05"]/strong/text()').extract()
        refPrice = response.xpath('//div[@class="right_box"]/div[@id="right_box_zj"]/p/span[2]').xpath('string(.)').extract()
        avePrice = response.xpath('//div[@class="right_box"]/div[@class="right_box_lpj"]/p/span[@class="cl_666"]/span/text()').extract()
        sub = response.xpath('//div[@class="right_box"]/div[3]/div[@class="right_box_zzlxnr"]/ul[@class="right_box_zzlxnrl hidden"]/li[@class="f14"]')
        area = response.xpath('//div[@class="right_box"]/div[3]/div[@class="right_box_zzlxnr"]/ul[@class="right_box_zzlxnrl hidden"]/li[@class="f14 w700"]/span[2]/a/text()').extract()
        street = response.xpath('//div[@class="right_box"]/div[3]/div[@class="right_box_zzlxnr"]/ul[@class="right_box_zzlxnrl hidden"]/li[@class="f14 w700"]/span[2]/a/text()').extract()
        position = response.xpath('//div[@class="right_box"]/div[3]/div[@class="right_box_zzlxnr"]/ul[@class="right_box_zzlxnrl hidden"]/li[@class="f14 w700"]/a/text()').extract()
        face = response.xpath('//div[@class="right_box"]/div[3]/div[@class="right_box_zzlxnr"]/div[@class="right_box_zzlxnrr_more"]/ul[1]/li[1]/text()').extract()
        unit = response.xpath('//div[@class="right_box"]/div[3]/div[@class="right_box_zzlxnr"]/div[@class="right_box_zzlxnrr_more"]/ul[1]/li[2]/text()').extract()
        if re.findall(re.compile(u'(.*?)新房'),estateArea[0])[0]:
            items['EstateArea'] = re.findall(re.compile(u'(.*?)新房'),estateArea[0])[0]
        if louPanName:
            items['LouPanName'] = louPanName[0]
        if unitNum:
            items['UnitNum'] = unitNum[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
        if refPrice:
            items['RefPrice'] = (float)(re.findall(re.compile(u'(\d.*?)万'),refPrice[0])[0])
        if avePrice:
            items['AvePrice'] = (float)(avePrice[0])
        if sub[0].xpath('string(.)').extract():
            items['Mortgage'] = sub[0].xpath('string(.)').extract()[0]
        if sub[1].xpath('string(.)').extract():
            items['HuXing'] = (float)(re.findall(re.compile(u'建面(\d.*?)㎡'),sub[1].xpath('string(.)').extract()[0].replace('\r','').replace('\n','').replace('\t','').replace(' ',''))[0])
        if sub[2].xpath('string(.)').extract():
            items['LouDong'] = sub[2].xpath('string(.)').extract()[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
        if sub[3].xpath('string(.)').extract():
            items['Floor'] = sub[3].xpath('string(.)').extract()[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
        if sub[4].xpath('string(.)').extract():
            items['BuildCate'] = sub[4].xpath('string(.)').extract()[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
        if area:
            items['Area'] = area[0]
        if street:
            items['Street'] = street[0]
        if position:
            items['Position'] = position[0]
        if face:
            items['Face'] = face[0]
        if unit:
            items['Unit'] = unit[0]
        items['LouPanUrl'] = response.url
        items['CrawlTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        yield items
