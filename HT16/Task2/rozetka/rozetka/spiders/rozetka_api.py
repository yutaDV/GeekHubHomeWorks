import scrapy


category = 'headphones/c80027'

class RozetkaApiSpider(scrapy.Spider):
    name = 'rozetka_api'
    allowed_domains = ['rozetka.com.ua']
    start_urls = [f'https://rozetka.com.ua/ua/{category}']


    def parse(self, response):
        for link in response.css('div.goods-tile a::attr(href)'):
            yield response.follow(link, callback=self.parse_product)

    def parse_product(self, response):
        yield{
            'ID': response.css('p.product__code.detail-code::text').get()[1:],
            'name': response.css('h1.product__title::text').get(),
            'price': response.css('p.product-prices__big::text').get(),
            'old_price': response.css('p.product-prices__small.ng-star-inserted::text')[0].get()[:-1],
            'currency': response.css('span.product-prices__symbol::text').get(),
            'is available': response.css('p.status-label.status-label--green.ng-star-inserted::text').get()[:-1]
        }
