# -*- coding: utf-8 -*-

import scrapy


class Offer(scrapy.Item):
  url = scrapy.Field()
  title = scrapy.Field()
  images = scrapy.Field()
  description = scrapy.Field()
  rooms = scrapy.Field()
  area = scrapy.Field()
  address = scrapy.Field()
  characteristics = scrapy.Field()
