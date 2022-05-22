import scrapy, unicodedata
from ..items import FlatsItem

class BytyroudnaSpider(scrapy.Spider):
    name = 'bytyroudna'
    allowed_domains = ['www.bytyroudna.cz']
    start_urls = ['http://www.bytyroudna.cz/']

    def parse(self, response):
        for row in response.xpath('//*[@id="cenik"]/div[1]/table/tbody/tr'):
            #item = FlatsItem()
            item = {}
            item['project'] = "Byty Roudna"
            item['id'] = int(row.xpath('td[1]//text()').extract_first())
            item['rooms'] = row.xpath('td[2]//text()').extract_first()

            area = row.xpath('td[3]//text()').extract_first()
            item['area'] = unicodedata.normalize('NFKD', area).rstrip(' m')

            item['price'] = row.xpath('td[5]//text()').extract_first().rstrip('Kč').replace(" ", "")

            item['availability'] = row.xpath('td[6]//text()').extract_first()
            item['type'] = "flat" if item['rooms'] != "nebytový prostor" else "non-residential"

            yield item
