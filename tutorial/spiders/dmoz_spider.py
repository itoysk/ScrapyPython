# -*- coding: utf-8 -*-

import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
       #, "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
       # filename = response.url.split("/")[-2]
      #  with open(filename,'wb') as f:
       #     f.write(response.body)
       # for sel in response.xpath('//ul/li'):
         for sel in response.xpath('//div[@class="title-and-desc"]'):
            item = DmozItem()
            item['title'] = sel.xpath('.//a/div/text()').extract()
            item['link'] = sel.xpath('.//a/@href').extract()
            item['desc'] = sel.xpath('.//div[@class="site-descr "]/text()').extract()
            yield item
            # print tt
