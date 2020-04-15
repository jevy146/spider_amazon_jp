import base64

import pymongo
import requests

mongodb_conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db_conn=mongodb_conn.amazon_Canada
table_conn=db_conn.amazon_Canada_goods



'''读取excel中的ASIN 获取没有爬取的ASIN'''


import pandas as pd


df=pd.read_excel('./Asin_Link/加拿大产品流量词.xlsx',encoding='utf-8')
all_asin=df['#1 已点击的 ASIN'][:10]

searchAsin=set()  #定义一个空的集合
for find_each in table_conn.find({},{'_id':0}):
    print(find_each)
    searchAsin.add(find_each['ASIN'])

'''补集，漏爬取的ASIN'''
miss_asin=[ each for each in all_asin if each not in searchAsin]
print(miss_asin)

import redis
conn = redis.Redis(host='192.168.31.104', port=6379, )

for each in miss_asin: #添加数据
    try :
        each=int(each) #过滤掉纯数字的ASIN，
        print(each)
    except:
        each='https://www.amazon.ca/dp/'+each
        print(each)
        conn.lpush('Detail_Canada:start_urls',each)





'''传递MongoDB的数据，保存相应的图片'''
def save_picture(find_each):
    fn = open(f"./picture/{find_each['ASIN']}.jpg", 'wb')
    print(f"正在下载{find_each['ASIN']}的图片")
    url_jpg=find_each['img']
    ret=url_jpg.startswith('https://images',beg=0,end=20) #判断链接的形式，前20个字符是否以"http"开头
    if ret:
        img_res=requests.get(url_jpg)
        fn.write(img_res.content)
    else:
        str2 = url_jpg.split(',')[-1]
        img_data = base64.b64decode(str2)
        fn.write(img_data)
    fn.close()
    return


# url_jpg='https://images-na.ssl-images-amazon.com/images/I/51RpoTL55BL._AC_SY300_.jpg'
# ret=url_jpg.startswith('https://images',)
# print(ret)

