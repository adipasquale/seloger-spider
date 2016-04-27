from flask import Flask
from flask import request

app = Flask(__name__)

SCRAPYRT_ENDPOINT = "http://localhost:9080/crawl.json"


@app.route("/api/v1/received_seloger_mail")
def crawl_and_mail():
  puts "received %s" % request

  if not (request.args.get("url")):
    raise Exception("missing args")

  r = requests.post(SCRAPYRT_ENDPOINT, json={
    "request": {
      "url": request.args.get("url"),
    },
    "spider_name": "seloger"
  })

  return "true"


if __name__ == "__main__":
  app.run(debug=True)
