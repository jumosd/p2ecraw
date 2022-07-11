from email import header
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import openpyxl
import os
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fuction_set import detailpagelist


from urllib.request import urlretrieve




options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
                    
# detail_lists = detailpagelist()
# def imgdown():
detail_lists = ['https://playtoearn.net/blockchaingame/axie-infinity']

url = detail_lists[0]
driver=webdriver.Chrome('./chromedriver 5',options=options) 
driver.get(url)
driver.implicitly_wait(1000)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# icon_img = soup.select_one("div.dapp_profilepic > img")['src']

icon_img = driver



