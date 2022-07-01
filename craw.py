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
sheet.append(["순위","게임이름", "장르", "네트워크", "디바이스", "NFT사용유무", "무료플레이", "얻을수있는것"])

url = 'https://playtoearn.net/blockchaingames/All-Blockchain/All-Genre/Live/All-Device/All-NFT/All-PlayToEarn/All-FreeToPlay'


driver=webdriver.Chrome('./chromedriver 5') 
driver.get(url)
#  로딩이 끝날때 까지 기다려주세요 
driver.implicitly_wait(1000)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')



elements = soup.select('body > div.container > div.indexmaintable.indexpage > div > table.table.table-bordered.mainlist > tbody > tr')

p2egame_list = {
    'name' :[],
    'genre' :[],
    'network' :[],
    'device' :[],
    'NFT' :[],
    'F2P' :[],
    'P2E' :[],
    

}
rank_num = -1

for idx , element in enumerate(elements):
    
    if element is not None:

        name = element.select_one('tbody > tr > td > a > div.dapp_name > span:nth-child(1)').string
        p2egame_list['name'].append(name)

        genre_list = []
        network_list= []
        device_list= []
        
        F2P_list= []
        P2E_list= []
        
        

        genres = element.select('td:nth-child(4) > a')
        for i in genres:
            genre = str(i.string)
            genre_list.append(genre)

        networks = element.select('td:nth-child(5) > a')
        for i in networks:
            network = i.attrs['data-original-title']
            network_list.append(network)

        devices = element.select('td:nth-child(6) > a')
        for i in devices:
            device = i.attrs['data-original-title']
            device_list.append(device)

        

       

        nft = element.select_one('td:nth-child(8) > a').string
        p2egame_list['NFT'].append(nft)

        f2p = element.select_one('td:nth-child(9) > a').string
        p2egame_list['NFT'].append(f2p)

        p2es = element.select('td:nth-child(10) > a')
        for i in p2es:
            p2e = i.string
            P2E_list.append(p2e)


        genre_list_str = ','.join(genre_list)
        genre_list_str = str(genre_list_str)

        network_list_str = ','.join(network_list)
        network_list_str = str(network_list_str)

        device_list_str = ','.join(device_list)
        device_list_str = str(device_list_str)

        P2E_list_str = ','.join(P2E_list)
        P2E_list_str = str(P2E_list_str)

        p2egame_list['genre'].append(genre_list_str)
        p2egame_list['network'].append(network_list_str)
        p2egame_list['device'].append(device_list_str)
        p2egame_list['P2E'].append(P2E_list_str)
        
        rank_num += 1 
        if  idx != 0:   
            sheet.append([rank_num,name,genre_list_str,network_list_str,device_list_str,nft,f2p,P2E_list_str])

        print(f"순위: {rank_num}    게임이름: {name}  장르: {genre_list_str}  네트워크: {network_list_str}  디바이스: {device_list_str}  NFT: {nft}  F2P: {f2p} P2E: {P2E_list_str}")
    
    
    else:
        None

    game_num = len(p2egame_list['name'])
    
    # 이지랄을 페이지를 전부다 탐색해야됨 !!
    # 이지랄을 페이지를 전부다 탐색해야됨 !!
    # 이지랄을 페이지를 전부다 탐색해야됨 !!
    # 이지랄을 페이지를 전부다 탐색해야됨 !!
    # 이지랄을 페이지를 전부다 탐색해야됨 !!

print( str(game_num - 1) + "개")
# wb.save("excel_1.xlsx")5

#  정규표현식  게임이름 URL에 넣기위해 변형한다
for idx, game_name in enumerate(p2egame_list['name']):
    if idx != 0:
        txt=game_name.replace(' ','-')
        txt=txt.replace('.','')
        txt=txt.replace(':','-')
        txt=txt.replace('!','')
        print(txt)


        detail_pages= f'https://playtoearn.net/blockchaingame/{txt}'
        print(detail_pages)