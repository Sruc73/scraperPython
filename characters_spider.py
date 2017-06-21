import scrapy


class BlogSpider(scrapy.Spider):
    name = "blogspider"
    start_urls = [
        'https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animation',
    ]

    def parse(self, response):
        for character in response.css('div#mw-pages div.mw-content-ltr li'):
            yield {
                'character': quote.css('a ::text').extract_first(),
            }
