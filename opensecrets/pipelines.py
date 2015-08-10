# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class OpensecretsPipeline(object):
    def process_item(self, item, spider):
        for key in item.keys():
            if key not in ['industry','funds']:
                if type(item[key])==list:
                    if len(item[key])>0:
                        item[key]=item[key][0]
        for fund,ind in zip(item['funds'],item['industry']):
            row={key:item[key] for key in item.keys() if key not in ['funds', 'industry']}
            row['funds']=fund
            row['industry']=ind
        item=row
        return item
