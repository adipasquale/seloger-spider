import scrapy

from seloger.items import Offer

class SeLogerSpider(scrapy.Spider):
  name = "seloger"
  allowed_domains = ["seloger.com"]
  start_urls = [
    "http://www.seloger.com/annonces/locations/appartement/torcy-77/beauregard-les-gradins/107404209.htm?ci=770468&idtt=1&idtypebien=1,9"
  ]

  def get_meta(self, name):
    return response.xpath('//meta[@property="og:%s"]/@content' % name).extract()[0]

  def parse(self, response):
    offer = Offer()
    offer["title"] = response.xpath('//meta[@property="og:title"]/@content').extract()[0]
    offer["description"] = response.xpath('//meta[@property="og:description"]/@content').extract()[0]
    offer["images"] = response.xpath('//img[@class="carrousel-img"]/@src').extract()
    yield offer
