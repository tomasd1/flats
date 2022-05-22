# flats-scraper
Simplistic/naive (no data validation, no synching, simply starts afresh each time) web scraper.
Scrapes data about available flats into MongoDB - example for BytyRoudna website.

Scrapy & MongoDB & pydantic


Spider for BytyRoudna can be launched from command line as follows:

scrapy crawl -s MONGODB_URI="<<CONNECTION STRING>>" -s MONGODB_DATABASE="db_name" bytyroudna