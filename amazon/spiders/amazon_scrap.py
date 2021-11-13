import scrapy
from ..items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        'https://www.amazon.in/s?k=one+%2Bplus&crid=VOQVURIJO2AI&sprefix=one+%2Caps%2C342&ref=nb_sb_ss_ts-doa-p_1_4'
    ]

    def parse(self,response):
        items = AmazonItem() 
        product_name = response.css('.a-size-medium.a-text-normal').css('::text').extract()
        product_reviews = response.css('.a-size-small .a-size-base').css('::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()

        # storing the data inside ItemContainers and later storing them inside mongo(pipelines.py - code for mongo class)
        items['product_name'] = product_name
        items['product_reviews'] = product_reviews
        items['product_price'] = product_price

        yield items

        next_page = 'https://www.amazon.in/s?k=one+%2Bplus&page='+str(AmazonSpider.page_number)+'&crid=VOQVURIJO2AI&qid=1629089471&sprefix=one+%2Caps%2C342&ref=sr_pg_2'

        # hardcoded the page number given in the url  
        # it will follow the next page until the code gets exhausted 
        if AmazonSpider.page_number<=20:
            AmazonSpider.page_number+=1
            yield response.follow(next_page,callback = self.parse)
