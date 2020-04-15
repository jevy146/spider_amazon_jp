# -*- coding: utf-8 -*-

# @File    : add_data_to_redis.py
# @Date    : 2019-10-25
# @Author  : ${杨杰伟}

#
import redis
conn = redis.Redis(host='192.168.31.104', port=6379, )
# import pymongo
#
# mongocli = pymongo.MongoClient(host="127.0.0.1", port=27017)
# # 创建mongodb数据库名称
# dbname = mongocli["amazon_jp"]
# # 创建mongodb数据库youyuan的表名称
# sheet_name = dbname["word_jp"]
# res=sheet_name.find()
# from urllib import request
# import re
# for each in res:
#     str_word = re.findall('k=(.*?)&', each["url"], re.S)[0]
#
#     if 'Sponsored' not in each['link_detail']:
#         print(each['link_detail'], request.unquote(str_word))
#         conn.lpush('Detail:start_urls',each['link_detail'])

conn.lpush('Detail:start_urls','https://www.amazon.co.jp/dp/B019IWZ75I')

