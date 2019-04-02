'''with open ('E:\\安装包\chrome下载\\china-city-list.csv','r',encoding='utf-8', errors='ignore') as f:
    city_list = f.readlines()
import requests
import time
url ='''
import requests
import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
book_weather = client['weather']
sheet_weather = book_weather['sheet_weather_3']
with open('E:\\安装包\\chrome下载\\china-city-list.csv','r',encoding='utf-8') as f:
    citylist = f.readlines()
    f.close()
for i in range(2):
    citylist.remove(citylist[0])
for i in citylist:
    url = 'https://free-api.heweather.net/s6/weather/forecast?localtion=' + i[0:11] + '&key=532c9899e18c43518dc92b05992b1fb8'
    city_html=requests.get(url)
    city_html.encoding = 'utf-8'
    time.sleep(1)
    dic = city_html.json()
    sheet_weather.insert_one(dic)
    



