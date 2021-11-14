from selenium import webdriver
from time import sleep
import cv2
import urllib.request
import numpy as np
from selenium.common.exceptions import NoSuchElementException
url="https://www.gettyimages.in/photos/shah-rukh-khan"
browser=webdriver.Edge(r"C:\Users\Swati Lohiya\Downloads\edgedriver_win64\msedgedriver.exe")
browser.get(url)
page1=browser.find_element_by_xpath("/html/body/div[2]/section/div/main/div/div/div[3]/div[2]")
for i in range(100):
    for j in range(1,5):
        try:
            img=browser.find_element_by_xpath('/html/body/div[2]/section/div/main/div/div/div[3]/div[2]/div[3]/div['+str(j)+']/article/a/figure/img')
            urllib.request.urlretrieve(img.get_attribute("src"),"local-filename"+str(i*j)+".jpg")
        except NoSuchElementException:
            pass
    if i==0:
        page1=browser.find_element_by_xpath("/html/body/div[2]/section/div/main/div/div/div[3]/div[2]/section/a")  
    else:
        page1=browser.find_element_by_xpath("/html/body/div[2]/section/div/main/div/div/div[3]/div[2]/section/a[2]")
    page1.click()
    sleep(4)
browser.close()