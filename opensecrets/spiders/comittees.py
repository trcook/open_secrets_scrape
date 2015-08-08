# -*- coding: utf-8 -*-
import scrapy
from opensecrets.items import ComitteeFunds
import logging
import re

class ComitteesSpider(scrapy.Spider):
    name = "comittees"
    allowed_domains = ["www.opensecrets.org"]
    start_urls = (
        'http://www.opensecrets.org/cmteprofiles/',
    )
    def parse(self, response):
        out=["http://www.opensecrets.org%s"% i for i in response.xpath('//form//option/@value').extract()]
        out=[re.sub('overview','profiles',i) for i in out]
        logging.log(logging.DEBUG, out)
        # out=[out[10]]
        print out
        for i in out:
            logging.log(logging.DEBUG, 'sending to pull %s' %i)
            years=range(105,115)
            for j in years:
                i=re.sub('congno=\d{3}',"congno=%s"%j,i)
                request= scrapy.Request(i,callback=self.pull_numbers)
                request.meta['year']=j
                yield request

    def pull_numbers(self,response):
        year=response.meta['year']
        members=response.xpath("//div[following-sibling::table[1]]/span/text()").extract()
        members=[re.findall('^.+to (.+?$)',i) for i in members]
        comittee=response.xpath('//h1[1]/text()').extract()
        for i in range(len(members)):
            logging.log(logging.DEBUG,'iteration %s'%i)
            member=members[i]
            logging.log(logging.DEBUG,'member: %s'%member)
            industry=response.xpath('//table[preceding-sibling::div[1] and position()=%s]//tr/td[position()=1]/text()'%i).extract()
            funds=response.xpath('//table[preceding-sibling::div[1] and position()=%s]//tr/td[position()=2]/text()'%i).extract()
            scrapy_record=ComitteeFunds()
            scrapy_record['member']=member
            scrapy_record['comittee']=comittee
            scrapy_record['funds']=funds
            scrapy_record['industry']=industry
            scrapy_record['year']=year
            yield scrapy_record





