# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import json
from openpyxl import Workbook
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class ExamplePipeline(object):
    def __init__(self):
        #打开文件
        self.file = open('HouseRent.json', 'w', encoding='utf-8')
    #该方法用于处理数据
    def process_item(self, item, spider):
        #读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #写入文件
        self.file.write(line)
        #返回item
        return item
    #该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass
    #该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass

class ToExcelPipeline(object):

    def __init__(self):
        #打开文件
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['标题', '网址', '价格', '面积', '出租房间'])  # 设置表头
    #该方法用于处理数据
    def process_item(self, item, spider):
        line = [item['title'], item['url'], item['price'], item['area'], item['rent']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('tuniu.xlsx')  # 保存xlsx文件
        return item
    #该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass
    #该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass