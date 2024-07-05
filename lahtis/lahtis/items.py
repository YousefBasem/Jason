# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LahtisItem(scrapy.Item):
    Name = scrapy.Field()
    Year = scrapy.Field()
    Make = scrapy.Field()
    Model = scrapy.Field()
    Trim = scrapy.Field()
    retailPrice = scrapy.Field()
    finalPrice = scrapy.Field()
    # year_number = scrapy.Field()
    # title = scrapy.Field()
    # article_number = scrapy.Field()
    # publish_date = scrapy.Field()
    # publish_date_epoch = scrapy.Field() #only for SQS
    # authors = scrapy.Field()
    # abstract = scrapy.Field()
    # keywords = scrapy.Field()
    
    # uid = scrapy.Field()
    # additional_metadata_from_xml = scrapy.Field()
    # html_full_text = scrapy.Field()
    # epic_ingest_hash = scrapy.Field()
    # journal = scrapy.Field()
    # source_filetype = scrapy.Field()
    # pdf_bytes = scrapy.Field()
    # pdf_needs_ocr = scrapy.Field()
    # pdf_filetype = scrapy.Field() #In theory this should always be 'application/pdf', but leaving this for added file flexibility
    # duplicate = scrapy.Field()
    # bucket = scrapy.Field()
    # s3_key = scrapy.Field()
    # pdf_downloaded = scrapy.Field()
    # valid_file = scrapy.Field()
    # text_layer_present = scrapy.Field()
