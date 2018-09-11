# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 02:26:59 2018

@author: Harsh Kava
"""

#for downloading file from link
import urllib.request
urllib.request.urlretrieve("https://s3.amazonaws.com/orim-misc-data/assessment/books.bson", "books.bson")

import bson
import json
import csv

with open('books.bson','rb') as f:
    data = bson.decode_all(f.read())
    type(data)    

columns =['title','primary_isbn','asin','apple_ean','google_id','publisher',
         'bisac_status','pub_date','price','series_name','volume','legacy_slugs', 'image', 'description']

column_header = ['title','primary_isbn13','asin','apple_ean','google_id','publisher','bisac_status',
                 'pub_date','us_list_price','series_name','volume','legacy_slugs', 'image', 'description', 'retailer','product_uri']
    
with open('dict.csv', 'w',newline='') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(column_header)
    for d in data:
        try:
            common_record = []
            for col in columns:
                if col in d.keys():
                    common_record.append(d.get(col))
                else:
                    common_record.append('')
                    
            a = d.get('retailer_site_links')
            if a is not None:
                retailer_links = list(a.values())
                retailer_links = retailer_links[0]
                for r in retailer_links:
                    retailer = r.get('name')
                    product_uri = r.get('url')
                    entry = []
                    entry = common_record + [retailer,product_uri]
                    writer.writerow(entry)
        except Exception as e:
            print('Exception is ::',e)