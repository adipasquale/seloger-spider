# Local Setup
mkvirtualenv seloger
pip install -r requirements.txt

# Run spider on single page for debugging

    workon seloger
    cd seloger
    MAILGUN_DOMAIN=... MAILGUN_API_KEY=... scrapy crawl seloger


# Run scrapyrt + flask server locally

    ./bin/run_local_server & python flask-api/app.py

# Images url schema

img
http://2.visuels.poliris.com/c175/2/7/1/a/271a17d0-3aa1.jpg
http://2.visuels.poliris.com/bigs/2/7/1/a/271a17d0-3aa1.jpg

