# -*- coding: utf-8 -*-

import scrapy

from seloger.items import Offer

IGNORE_WORDS_IN_TITLE = [
  u"Location", u"Appartement", u"2 pièces", u"appartement F2/T2/2 pièces"
]

class SeLogerSpider(scrapy.Spider):
  name = "seloger"
  allowed_domains = ["seloger.com"]
  start_urls = [
    "http://www.seloger.com/annonces/locations/appartement/paris-3eme-75/enfants-rouges/108976823.htm?"
  ]

  def get_meta(self, name):
    return response.xpath('//meta[@property="og:%s"]/@content' % name).extract()[0]

  def parse(self, response):
    offer = Offer()
    offer["url"] = response.url
    offer["title"] = response.xpath('//meta[@property="og:title"]/@content').extract()[0]
    for word in IGNORE_WORDS_IN_TITLE:
      offer["title"] = offer["title"].replace(word, "")
    offer["title"].strip()
    offer["description"] = response.xpath('//meta[@property="og:description"]/@content').extract()[0].strip()
    offer["images"] = response.css('.carrousel_image_small::attr("src")').extract()
    offer["characteristics"] = response.css(".liste__item-switch, .liste__item-float, .liste__item").xpath("text()").extract()
    offer["characteristics"] = [c.strip() for c in offer["characteristics"] if "DPE" not in c and "GES" not in c and c.strip()]
    yield offer
