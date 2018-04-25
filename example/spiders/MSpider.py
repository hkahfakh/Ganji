# -*- coding: utf-8 -*-

import scrapy
from example.items import ExampleItem
import json
     #设置name
class MSpider(scrapy.Spider):
    name = "MySpider"
    #设定域名
    allowed_domains = ["bj.ganji.com"]
    #填写爬取地址
    start_urls = ["http://bj.ganji.com/fang1/o1","http://bj.ganji.com/fang1/o2"]
    #编写爬取方法rtr
    def parse(self, response):

        with open('data.json', 'wb') as f:
            f.write(response.body)

        item = ExampleItem()

        for box in response.xpath('//div[@class="f-list-item ershoufang-list"]'):
            #获取div中的课程标题
            item['title'] = box.xpath('.//dd[@class="dd-item title"]/a[@class="js-title value title-font"]/text()').extract()[0]
            #获取div中的价格
            item['price'] = box.xpath('.//dd[@class="dd-item info"]/div[@class="price"]/span[@class="num"]/text()').extract()[0]
            #获取房屋面积
            item['area'] = box.xpath('.//dl[@class="f-list-item-wrap f-clear"]/dd[@class="dd-item size"]/span[5]/text()').extract()[0]
            #房屋租赁方式
            item['rent'] = box.xpath('.//dl[@class="f-list-item-wrap f-clear"]/dd[@class="dd-item size"]/span[@class="first js-huxing"]/text()').extract()[0]
            yield item

        next_page = 'http://bj.ganji.com' + response.css('div.pageBox')[1].xpath('.//a[@class="next"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, headers={'referer': next_page})



