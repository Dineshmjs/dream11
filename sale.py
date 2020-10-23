
from selenium import webdriver
import pymongo

# import time
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/home/spe/Desktop/python/dream11/chromedriver/chromedriver")
driver.get("https://in.event.mi.com/in/diwali-with-mi-2020-sale")

button = "/html[1]/body[1]/div[1]/div[20]/div[1]/div[4]/div[1]/div[2]/ul[1]/li[1]/div[2]/div[1]/div[2]/a[1]"
driver.find_element_by_xpath(button).click()