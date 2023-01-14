import requests
import sqlite3
from bs4 import BeautifulSoup

url = ''

response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text, 'html.parser')

#賃料
rent_fee = bs.find(class_='property_view_main-emphasis').text.strip().rstrip("万円")

#概要
bs_property_data_titles = bs.find_all(class_='property_data-title')
property_data_titles =[]
for ele in bs_property_data_titles:
    property_data_titles.append(ele.text)

bs_property_data_bodys = bs.find_all(class_='property_data-body')
property_data_bodys =[]
for ele in bs_property_data_bodys:
    property_data_bodys.append(ele.text.strip())

for i,ele in enumerate(property_data_titles):
    if ele == '間取り':
        plan_of_a_house = property_data_bodys[i]
    elif ele == '専有面積':
        exclusive_area = property_data_bodys[i]
    elif ele == '建物種別':
        building_Type = property_data_bodys[i]
    elif ele == '築年数':
        number_of_years_of_construction = property_data_bodys[i]



#詳細データ
bs_detail_head_datas = bs.find(class_='data_table table_gaiyou').find_all('th')
detail_head_datas = []
for ele in bs_detail_head_datas:
    detail_head_datas.append(ele.text)

bs_detail_datas = bs.find(class_='data_table table_gaiyou').find_all('td')
detail_datas = []
for ele in bs_detail_datas:
    detail_datas.append(ele.text.strip())

#設備
equipments = bs.find(class_='section l-space_small').find('li').text

print("fin")