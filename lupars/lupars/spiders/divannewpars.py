import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lus = response.css("div._Ud0k")
        for lu in lus:
            yield {
                "name" : lu.css("div.lsooF span::text").get(),
                "price" : lu.css("div.pY3d2 span::text").get(),
                "url" : lu.css("a").attrib["href"]
            }