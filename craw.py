import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import openpyxl


# 2. 내가 작업할 Workbook 생성하기 
wb = openpyxl.Workbook()
# 3. 작업할 Workbook 내 Sheet 활성화 
sheet = wb.active
# 4. Sheet 내 Cell 선택 (A1셀에 1이라는 값 할당) 
sheet.append(["순위","게임이름", "장르", "네트웤"])

url = 'https://playtoearn.net/blockchaingames/All-Blockchain/All-Genre/Live/All-Device/All-NFT/All-PlayToEarn/All-FreeToPlay'



driver=webdriver.Chrome('./chromedriver 5') 
driver.get(url)
 #로딩이 끝날때 까지 기다려주세요 
driver.implicitly_wait(1000)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

elements = soup.select('body > div.container > div.indexmaintable.indexpage > div > table.table.table-bordered.mainlist > tbody > tr')

p2egame_list = {
    'name' :[],
    'genre' :[],
    'network' :[],

}
rank_num = 0

for element in elements:
    
    if element is not None:

        name = element.select_one('tbody > tr > td > a > div.dapp_name > span:nth-child(1)').string
        genres = element.select('td:nth-child(4) > a')
        genre_num = len(genres)
        print("------------------------------------------------------------------------------------------")
        print(len(genres))
        

        p2egame_list['name'].append(name)

        genre_list =[]
        for i in genres:
            genre = str(i.string)
            genre_list.append(genre)

        
        genre_list_str = ','.join(genre_list)
        genre_list_str = str(genre_list_str)
        
        p2egame_list['genre'].append(genre_list_str)
        
        
    
        rank_num += 1    
        sheet.append([rank_num,name,genre_list_str, ''])

        print(f"순위: {rank_num}    게임이름: {name}    장르: {genre_list_str} ")
    
    
    else:
        None

    game_num = len(p2egame_list['name'])

print( str(game_num) + "개")
wb.save("excel_1.xlsx")
