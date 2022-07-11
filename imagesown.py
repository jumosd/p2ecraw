#웹드라이버
from selenium import webdriver
# By를 임포트해서 선택자를 선택할수있다
from selenium.webdriver.common.by import By
# Os를 임포트에 저장할수있다
import os
# urlretrieve 를이용 'src' 다운
from urllib.request import urlretrieve
# 씨발 드디어찾앗다.. 디로드.... 이걸로 받자..403에러는 이걸로.. src따서 바로 ㄱㄱ 
import dload


import time
 
options = webdriver.ChromeOptions()
options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"')
    

driver=webdriver.Chrome('./chromedriver 5', options = options) 
driver.get("https://playtoearn.net/blockchaingame/axie-infinity")
time.sleep(3)
 
icon_img = driver.find_element(By.CSS_SELECTOR, "div.dapp_profilepic > img")

img_url = []


icon_url = icon_img.get_attribute('src')
img_url.append(icon_url)
print(img_url)
 
#이미지를 저장할 폴더
img_down_folder = './Result/1_Axie Infinity'
# 폴더가없으면 폴더이름으로 생성
if not os.path.isdir(img_down_folder):
    os.mkdir(img_down_folder)

dload.save(icon_url, f'{img_down_folder}/i.jpg') 

# urlretrieve(url, img_down_folder )
driver.quit()

