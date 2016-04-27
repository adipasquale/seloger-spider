mkvirtualenv seloger
pip install -r requirements.txt


workon seloger

MAILGUN_DOMAIN=... MAILGUN_API_KEY=... scrapy crawl seloger
