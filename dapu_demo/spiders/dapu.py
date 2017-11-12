# -*- coding: utf-8 -*-
import scrapy
from dapu_demo.items import DapuDemoItem


class DapuSpider(scrapy.Spider):
    name = 'dapu'
    allowed_domains = ['www.dapu.com']
    start_urls = ['http://www.dapu.com/gallery-422.html']

    def parse(self, response):
        for sel in response.css('.goodspic div.goodtext'):
			item = DapuDemoItem()
			item['name'] = sel.css('p:first-of-type>span::text').extract_first()
			item['price'] = sel.css('p:last-of-type>a::text').extract_first()
			yield item
			print item['name'], item['price']
