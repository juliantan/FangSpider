# -*- coding: utf-8 -*-
import scrapy


class NewfangspiderSpider(scrapy.Spider):
    name = 'NewFangSpider'
    allowed_domains = ['www.fang.com']
    start_urls = ['http://www.fang.com/']

    def parse(self, response):
        pass
