#-*-coding:utf-8-*-

from scrapy import cmdline
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from FangSpider.spiders import NewFangSpider

# cmdline.execute("scrapy crawl LjSpider -o LjSpider.csv".split())
# cmdline.execute("scrapy crawl LjSpider -o LjSpider.xml".split())
# cmdline.execute("scrapy crawl LjSpider -o LjSpider.pickle".split())
# cmdline.execute("scrapy crawl LjSpider -o LjSpider.marshal".split())
# cmdline.execute("scrapy crawl LjSpider -o LjSpider.json".split())
# cmdline.execute("scrapy crawl LjSpider -o ftp://user:pass@ftp.example.com/path/to/LjSpider.csv".split())

settings = get_project_settings()
process = CrawlerProcess(settings=settings)
process.crawl(NewFangSpider.NewfangspiderSpider)

process.start()

