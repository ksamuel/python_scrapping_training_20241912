import scrapy
from scrapy.linkextractors import LinkExtractor


class DogSpiderCustomRules(scrapy.Spider):
    name = "dog_spider_custom_rules"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org"]

    def parse(self, response):
        extractor = LinkExtractor(allow=["/wiki/[^#:]+"])
        links = extractor.extract_links(response)
        for link in links:
            if "e" in link.url:
                yield scrapy.Request(link.url, callback=self.parse)

    def display_title(self, response):
        title = response.xpath("//h1/text()").get()
        if title:
            yield {"title": title}
