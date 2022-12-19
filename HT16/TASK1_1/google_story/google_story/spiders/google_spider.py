import scrapy

from bs4 import BeautifulSoup


class GoogleSpiderSpider(scrapy.Spider):
    name = 'google_spider'
    allowed_domains = ['chrome.google.com']
    start_urls = ['http://chrome.google.com/webstore/sitemap']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'xml')
        for item in soup.select('sitemap > loc'):
            yield scrapy.Request(item.text, callback=self.parse_more_links)

    def parse_more_links(self, response):
        soup = BeautifulSoup(response.text, 'xml')
        for item in soup.select('url > loc'):
            if not "/detail" in item.text: continue
            yield {
                'name': response.css('h1.e-f-w::text').get(),
                'description': response.css('div.C-b-p-j-Pb::text').get()
            }