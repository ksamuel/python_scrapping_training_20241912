from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DogSpider(CrawlSpider):
    name = "dog_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org"]

    rules = (
        Rule(
            LinkExtractor(allow=["/wiki/[^#:]+"]), callback="display_title", follow=True
        ),
    )

    def display_title(self, response):
        title = response.xpath("//h1/text()").get()
        if title:
            yield {"title": title}
