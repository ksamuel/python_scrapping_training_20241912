# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        with open("titles", "a", encoding="utf8") as f:
            f.write(item["title"] + "\n")
