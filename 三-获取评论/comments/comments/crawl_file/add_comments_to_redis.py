# -*- coding: utf-8 -*-

# @File    : add_comments_to_redis.py
# @Date    : 2019-12-17
# @Author  : ${杨杰伟}
import pymongo
import redis

conn = redis.Redis(host='192.168.31.104', port=6379, )
#
# one_link='https://www.amazon.com/product-reviews/B018364XAA/ref=acr_dpproductdetail_text?ie=UTF8&showViewpoints=72'
# conn.lpush('comments_info:start_urls', one_link)


import pandas as pd

import  numpy as np

def read_link(path):

    df_file = pd.read_excel(path, sheet_name=0, encoding="utf-8",header=None)
    return df_file

PATH="./工作簿1.xlsx"

PAGE_ASIN=np.array(read_link(PATH))  #读取所有的链接
print(PAGE_ASIN)
count=1
for two_list in PAGE_ASIN:
    for one_link in two_list:
        if str(one_link) == 'nan':
            pass
        else:
            print(one_link)
            count += 1
            conn.lpush('comments_info:start_urls', one_link)

print(count)


# mongocli = pymongo.MongoClient(host="127.0.0.1", port=27017)
# # 创建mongodb数据库名称
# dbname = mongocli["amazon_us"]
# # 创建mongodb数据库youyuan的表名称
# sheetname = dbname["amazon_us_comments"]
#
# search_df=[]
# for search in sheetname.find({}, {"_id": 0}):  #查询获取所有的信息
#     search_df.append(search['url'])
# print(search_df)
# link=search_df
# count=1
# for two_list in PAGE_ASIN:
#     for one_link in two_list:
#         if str(one_link) == 'nan':
#             pass
#         else:
#             print(one_link)
#             if one_link not in set(link):
#                 print(one_link)
#                 count += 1
#                 conn.lpush('comments_info:start_urls', one_link)
#
# print(count)

