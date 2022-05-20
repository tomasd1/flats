# flats-scraper
Simplistic/naive web scraper. Scrapes data about available flats into MongoDB - example for BytyRoudna website.

Python & Scrapy & MongoDB


Spider for BytyRoudna can be launched from command line as follows:

scrapy crawl -s MONGODB_URI="<<CONNECTION STRING>>" -s MONGODB_DATABASE="db_name" bytyroudna