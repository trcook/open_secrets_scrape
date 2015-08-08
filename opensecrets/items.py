# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ComitteeFunds(scrapy.Item):
    # define the fields for your item here like:
    funds = scrapy.Field()
    member= scrapy.Field()
    industry= scrapy.Field()
    comittee= scrapy.Field()
    year=scrapy.Field()