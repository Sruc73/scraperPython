import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animation',
    ]

    def parse(self, response):
        for quote in response.css('div#mw-pages div.mw-content-ltr li'):
            yield {
                'character': quote.css('a ::text').extract_first(),
            }
