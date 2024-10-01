from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions  import NoSuchElementException
url="https://www.etsy.com/in-en/listing/546737718/star-ear-crawler-earrings-925-sterling?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sr_gallery-1-8&bes=1"
browser=webdriver.Chrome("C:/Users/vinod/OneDrive/Desktop/New folder/chromedriver.exe")
browser.get(url)
a=[]
page1=browser.find_element_by_xpath("//*[@id='reviews']/div[2]/nav/ul/li[position()=last()]/a")
for j in range(1,51):
    
    for i in range(4):
        try:
            reviews=browser.find_element_by_xpath('//*[@id="review-preview-toggle-'+str(i)+'"]')
        
            a.append(reviews.text)
        except NoSuchElementException:
            pass
            
    page1=browser.find_element_by_xpath("//*[@id='reviews']/div[2]/nav/ul/li[position()=last()]/a")
    page1.click()
    sleep(4)

import sqlite3 as sql
import pandas as pd
df=pd.DataFrame()
df["reviews"]=a
df.to_csv("real_reviews2.csv",index=False)
conn=sql.connect("reviews2.db")
df.to_sql("real_reviews",conn,index=False)
curser=conn.cursor()
curser.execute("SELECT * FROM real_reviews")
for record in curser:
    print(record) 

