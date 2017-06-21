# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector

class BlogSpider(scrapy.Spider):
    name = "blogspider"
    start_urls = [
        'http://www.babelio.com/auteur/Frederic-Dard/7187/citations',
    ]

    def parse(self, response):
        for title in response.css('div.post_con div.text.row div'):
            yield {
                'quote': title.css('div ::text').extract_first()
            }

        next_page = response.css('div.pagination.row > a').extract()
        for index,page in enumerate(next_page):
            if 'class = "active"' in page:
                n_page = next_page[index + 1]
                next_page = selector(text=n_page).xpath('//a/@href').extract()
                next_page_url = next_page[0]
                if index == (len(next_page) - 1):
                    next_page = False

        if next_page:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
