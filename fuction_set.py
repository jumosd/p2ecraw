from openpyxl import  *

# data_only=True로 해줘야 수식이 아닌 값으로 받아온다.
def detailpagelist():
    load_wb = load_workbook("/Users/hajinsu/Documents/쌀먹프로젝트 1000억 매출/컨텐츠 자동화 연구소/자동화결과물/22_0710 p2e정보크롤링.xlsx", data_only=True)
    # 시트 이름으로 불러오기 
    load_ws = load_wb['Sheet']

    detail_page_sheet = list(load_ws.columns)[8]
    detail_page_list=[]
    for cell_obj in detail_page_sheet[1:]:

        detail_page_list.append(cell_obj.value)

    return detail_page_list

