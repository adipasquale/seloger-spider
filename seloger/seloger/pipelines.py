# -*- coding: utf-8 -*-

import requests
import os


class SendMail(object):
  def process_item(self, item, spider):

    images_html = "".join(["<li style='margin:10px;padding:0;display:inline;'><img src='%s' style='max-width:400px;' /></li>" % img for img in item["images"]])
    characteristics_html = "".join(["<li>%s</li>" % c for c in item["characteristics"]])
    html = """
      <b>%s</b>
      <p>%s</p>
      <ul style='list-style-type:none;margin:0;padding:0'>%s</ul>
      <ul style='list-style-type:none;margin-top:20px;padding:0'>%s</ul>
      <a href='%s'>%s</a>
      """ % (
        item["title"], item["description"], images_html, characteristics_html, item["url"], item["url"]
      )

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
