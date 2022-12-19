import scrapy

def input_category():

    result = input('Введіть назву та ID категорії через / (приклад:mobile-phones/c80003/)')
    return result

category = input_category()

class RozetkaApiSpider(scrapy.Spider):
    name = 'rozetka_api'
    allowed_domains = ['rozetka.com.ua']
    start_urls = [f'https://rozetka.com.ua/ua/{category}']


    def parse(self, response):
        for link in response.css('div.goods-tile a::attr(href)'):
            yield response.follow(link, callback=self.parse_product)

    def parse_product(self, response):
        yield{
            'name': response.css('h1.product__title::text').get(),
            'price': response.css('p.product-prices__big::text').get(),
            'currency': response.css('span.product-prices__symbol::text').get(),
        }
