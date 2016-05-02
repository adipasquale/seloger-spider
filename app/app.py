from flask import Flask
from flask import request
import re
import requests
import os
from raygun4py.middleware import flask

app = Flask(__name__)
if os.environ.get("RAYGUN_API_KEY"):
  print "attaching raygun ..."
  flask.Provider(app, os.environ["RAYGUN_API_KEY"]).attach()

SCRAPYRT_ENDPOINT = "http://localhost:9080/crawl.json"


@app.route("/api/v1/received_seloger_mail", methods=["POST"])
def crawl_and_mail():
  print "request.form is %s" % request.form["stripped-html"]
  urls = set(re.findall(r"www\.seloger.com/annonces/locations/[a-z0-9\/\-]+.htm\?", request.form["stripped-html"]))

  for url in urls:
    r = requests.post(SCRAPYRT_ENDPOINT, json={
      "spider_name": "seloger", "request": {"url": "http://%s" % url}
    })
    if r.status_code != 200:
      raise Exception("bad status code returned by scrapyRT : %s" % r.status_code)

  return "true"


if __name__ == "__main__":
  app.run(debug=True)
