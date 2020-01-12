import scrapy
import mysql.connector

def insert_to_db(quotes):
    #TODO: Transfer parameters to conf file
    #TODO: Transfer function to some sort of utils file
    cnx = mysql.connector.connect(user='root', password='senhasql',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='Crawlers')
    cursor = cnx.cursor()

    add_quote = ("INSERT INTO Quotes "
                  "(quote, author, tags) "
                  "VALUES (%(text)s, %(author)s, %(tags)s)")


    for quote in quotes:
        cursor.execute(add_quote,quote)

    cnx.commit()

    cursor.close()

    cnx.close()

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        '''Must return a list or generator of requests that will used to start
        the crawler first. Crawling will continue from these requests'''


        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''' How to deal with each response. Response is of type TextResponse.
        It holds the received page'''
        quotes =[]
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        #TODO: define quote class to assure consistency
        for quote in response.css("div.quote"):
            quotes.append({"text":quote.css("span.text::text").get(),
                        "author":quote.css("small.author::text").get() ,
                        "tags":",".join(quote.css("div.tags a.tag::text").getall())})
        insert_to_db(quotes)
