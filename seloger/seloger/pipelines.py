# -*- coding: utf-8 -*-

import requests
import os


class SendMail(object):
  def process_item(self, item, spider):

    images_html = "".join(["<li style='margin:10px;padding:0;display:inline;'><img src='%s' /></li>" % img for img in item["images"]])
    html = "<h1>%s</h1><p>%s</p><ul style='list-style-type:none;margin:0;padding:0'>%s</ul>" % (item["title"], item["description"], images_html)

    res = requests.post(
      'https://api.mailgun.net/v3/%s/messages' % os.environ["MAILGUN_DOMAIN"],
      auth=('api', os.environ["MAILGUN_API_KEY"]),
      data={
        'from': 'selogermail@selogermail.herokuapp.com',
        'to': "adrien.dipasquale@gmail.com",
        'subject': item["title"],
        'html': html
      }
    )
    if res.status_code != 200:
      raise Exception()
    return item
