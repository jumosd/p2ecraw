from asyncore import write
from webbrowser import BaseBrowser
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
import dload


from selenium.webdriver.chrome.service import Service




# DeleteAllFiles('./Result/')


# 2. 내가 작업할 Workbook 생성하기 
wb = openpyxl.Workbook()
# 3. 작업할 Workbook 내 Sheet 활성화 
sheet = wb.active
# 4. Sheet 내 Cell 선택 (A1셀에 1이라는 값 할당) 
sheet.append(["순위","게임이름", "장르", "네트워크", "디바이스", "NFT사용유무", "무료플레이", "얻을수있는것", "p2e사이트 상세페이지 링크"])

cur_page = 1
rank_num = 0

Folder_names = []



while cur_page <= 1:
    url = f"https://playtoearn.net/blockchaingames/All-Blockchain/All-Genre/Live/All-Device/All-NFT/All-PlayToEarn/All-FreeToPlay?sort=socialscore_24h&amp%3Bdirection=desc&amp%3Bpage=%7Bcur_page2&direction=desc&page={str(cur_page)}"
    
    
    
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
            
            detail_url =  element.find('a', {'class':'dapp_detaillink'}).attrs['href']

            driver.quit()
            if idx != 0:
                rank_num += 1
                
            

                try:
                    
                    
                    print(f"순위: {rank_num}    게임이름: {name}  장르: {genre_list_str}  네트워크: {network_list_str}  디바이스: {device_list_str}  NFT: {nft}  F2P: {f2p} P2E: {P2E_list_str} 상세링크: {detail_url}")
                    sheet.append([rank_num,name,genre_list_str,network_list_str,device_list_str,nft,f2p,P2E_list_str,detail_url])
                    
                    
                    Folder_name = (str(rank_num) + "_" + str(p2egame_list['name'][idx]))
                    # if 페이지를 가져오면 밑에꺼출력
                    os.mkdir('./Result/'+Folder_name)
                    Folder_names.append(Folder_name)
                    # # 이부분 이 이상
                    # req_get_txt = requests.get(detail_url).text
                    # print(req_get_txt)
                    # driver.get(detail_url)
                    # driver.implicitly_wait(10)

                    # try:
                    #     element = WebDriverWait(driver, 10).until(
                    #         EC.presence_of_element_located((By.CLASS_NAME, "owl-item"))
                    #     )
                    # finally:
                    #     driver.quit()
                    

                    # else 실패하면
                    #os.mkdir('./Result/' +str(a) + "_" + "사진X_" +str(p2egame_list['name'][a]))
                    continue

                except OSError:
                    # if e.errno != errno.EEXIST:
                    #     raise
                    # time.sleep might help here
                    pass
                
               
            None
            
    cur_page += 1

wb.save("excel_1.xlsx")


# data_only=True로 해줘야 수식이 아닌 값으로 받아온다.

load_wb = openpyxl.load_workbook("/Users/hajinsu/Documents/쌀먹프로젝트 1000억 매출/컨텐츠 자동화 연구소/excel_1.xlsx", data_only=True)
# 시트 이름으로 불러오기 
load_ws = load_wb['Sheet']

detail_page_sheet = list(load_ws.columns)[8]
detail_page_list=[]
for cell_obj in detail_page_sheet[1:]:

    detail_page_list.append(cell_obj.value)

load_wb.close()
# options = webdriver.ChromeOptions()
# options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"')
    
for detail,Folder_name in zip(detail_page_list ,Folder_names) :
    print(detail)
   
    time.sleep(5)
    service = Service('./chromedriver 5')
    driver=webdriver.Chrome('./chromedriver 5',service = service)
    
    driver.get(detail)
    
    
    
    icon_img = driver.find_element(By.CSS_SELECTOR, "div.dapp_profilepic > img")
    icon_url = icon_img.get_attribute('src')
    game_dec = driver.find_element(By.CSS_SELECTOR, "div.col-12.col-lg-8.col-xl-9 > div > p").text
    main_link = driver.find_element(By.CSS_SELECTOR, "body > div.container > div.details.gamepage > div > div > div:nth-child(1) > div > div.col-12.col-lg-4.col-xl-3 > div.social > a:nth-child(1) > div").get_attribute('href')
    # twitter_link = driver.find_element(By.CSS_SELECTOR, "div.col-12.col-lg-8.col-xl-9 > div > p").text



    print(main_link)
    f = open(f'./Result/{Folder_name}/dec.txt','w')
    f.write(game_dec)
    f.close()


    path = f'./Result/{Folder_name}'
    

    

    # 폴더가없으면 폴더이름으로 생성
    if not os.path.isdir(path):
        os.mkdir(path)
        

    dload.save(icon_url, f'{path}/icon.jpg')
    
    #이미지를 저장할 폴더

    # for Folder_name in Folder_names:
    #     img_down_folder = f'./Result/{Folder_name}'
    #     print('폴더이름: ' + img_down_folder)
    #     # 폴더가없으면 폴더이름으로 생성
    #     if not os.path.isdir(img_down_folder):
    #         os.mkdir(img_down_folder)

    #     dload.save(icon_url, f'{img_down_folder}/icon.jpg') 
    # driver.switch_to.window(driver.window_handles[-1])    

driver.quit()









# # 게임이름 URL에 넣기위해 변형한다
# detail_pages_url =[]
# for idx, game_name in enumerate(p2egame_list['name']):
#     if idx != 0:
#         txt=game_name.replace(' ','-')
#         txt=txt.replace('.','')
#         txt=txt.replace(':','-')
#         txt=txt.replace('!','')
#         txt=txt.replace('--','-')
#         txt=txt.replace('---','-')
#         txt=txt.replace('----','-')
#         detail_pages= f'https://playtoearn.net/blockchaingame/{txt}'
        
#         detail_pages_url.append(detail_pages)
# a = 0


# for url in detail_pages_url :

    
    
#     response = requests.get(url)
#     a += 1
#     print(response.status_code , a, url)
#     driver.get(url)
#     driver.implicitly_wait(1000)


#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')


      

#     images = driver.find_elements_by_css_selector(".owl-item.active")
    
#     count = 1
#     for image in images:
#         try: 
#             image.click()
#             time.sleep(2)
#             imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
#             urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
#             count = count + 1
#         except:
#             pass
 
# driver.close()