# -*- coding: utf-8 -*-

# @File    : 将MongoDB的数据取出保存为excel.py
# @Date    : 2019-12-31
# @Author  : ${杨杰伟}
import pymongo
import pandas as pd
#链接数据库
import  numpy as np

connection=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=connection['amazon_india']
db_table=db['amazon_india_kinds']

for search in db_table.find({},{'_id':0}):
    print(search)



def read_link(path):
    df_file = pd.read_excel(path, sheet_name=0, encoding="utf-8",header=None)
    return df_file
PATH="./crawl_file/工作簿1.xlsx" #爬取的书友链接
PAGE_ASIN=np.array(read_link(PATH))  #


search_set=set()
for two_list in PAGE_ASIN:
    for one_link in two_list:
        if str(one_link) == 'nan':
            pass
        else:
            search_set.add(one_link)
print(len(search_set))
print(search_set)

search_df=[]
for one_link in search_set:
    try:
        res = db_table.find({'url': one_link}, {'_id': 0})
        for search in res:  # 查询获取所有的信息
            print(search)
            search_df.append(search)
    except:
        pass



print('总计条数',len(search_df))
df1=pd.DataFrame(search_df)
print(df1.shape)
print(df1.columns)
df1.columns="ASIN,赞同数量,评论日期,评论人名,评论内容,评论标题,包装颜色,包装大小,星级,链接".split(',')
df1.to_excel('./detail_page/德国评论.xlsx',header=True,index=None)
df1.to_csv('./detail_page/德国评论.csv')
