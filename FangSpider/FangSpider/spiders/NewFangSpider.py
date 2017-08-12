# -*- coding: utf-8 -*-
import scrapy
import re
from FangSpider.items import FangspiderItem

class NewfangspiderSpider(scrapy.Spider):
    name = 'NewFangSpider'
    allowed_domains = ['www.fang.com']
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
        item = FangspiderItem()
        loupanlist = response.xpath('//div[@class="contentList fl clearfix"]/ul[@class="flist"]')
        for i in xrange(1,len(loupanlist)):
            item['Name'] = loupanlist[i-1].xpath('./li[1]/div[@class="finfo c_333_f14"]/h3/a/text()').extract()[0]
            item['HuXing'] = loupanlist[i-1].xpath('./li[1]/div[@class="finfo c_333_f14"]/p[@class="hx"]').xpath('string(.)').extract()[0].replace('\n','').replace('\t','').replace(' ','').split('|')[0]
            item['Face'] = loupanlist[i-1].xpath('./li[1]/div[@class="finfo c_333_f14"]/p[@class="hx"]').xpath('string(.)').extract()[0].replace('\n','').replace('\t','').replace(' ','').split('|')[1]
            item['Region'] = loupanlist[i-1].xpath('./li[1]/div[@class="finfo c_333_f14"]/p[@class="font_size14"]/a/span/text()').extract()[0]
            item['Loc'] = loupanlist[i-1].xpath('./li[1]/div[@class="finfo c_333_f14"]/p[@class="font_size14"]/span/text()').extract()[0]
            item['Area'] = loupanlist[i-1].xpath('./li[1]/div[@class="flist_right clearfix mt_-26"]/div[@class="mt8 alignR float_ri"]/p[1]/text()').extract()[0]
            item['TotalPrice'] = loupanlist[i-1].xpath('./li[1]/div[@class="flist_right clearfix mt_-26"]/div[@class="moreInfo float_ri"]/p[@class="danjia alignCenter"]/text()').extract()[0]
            item['UnitPrice'] = loupanlist[i-1].xpath('./li[1]/div[@class="flist_right clearfix mt_-26"]/div[@class="moreInfo float_ri"]/p[@class="alignCenter"]/span/text()').extract()[0]
            item['LoupanUrl'] = loupanlist[i-1].xpath('./li[1]/div[@class="finfo c_333_f14"]/h3/a/@href').extract()[0]
            item['CrawlTime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            yield item
        baseurl = re.findall(re.compile(r'.*?com'),response.url)[0]
        nextpageurl = baseurl+response.xpath('//div[@class="contentList fl clearfix"]/div[@id="sjina_D25_101"]/ul[@class="clearfix"]/li[@class="fr"]/a[@class="next"]/@href').extract()[0]
        yield scrapy.Request(nextpageurl,callback=self.parse)









