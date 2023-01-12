import requests
from bs4 import BeautifulSoup
import json
import os
import csv
import pandas as pd
#需要获取的省份个数
index = 10
result = {"地区" : [],
          "新增" : [],
          "现有" : [],
          "累计" : [],
          "治愈" : [],
          "死亡" : [],
          }
with open('data.html', 'r', encoding='utf-8') as f:
    Soup = BeautifulSoup(f.read(), 'html.parser')
    #获取各种数据
    for i in range(index):
        Names = Soup.select('body > div.common-container > div:nth-child(2) > div.wrap > ul > li:nth-child({}) > div > span.item_name'.format(i))
        News = Soup.select('body > div.common-container > div:nth-child(2) > div.wrap > ul > li:nth-child({}) > div > span.item_confirm > span'.format(i))
        Existings = Soup.select('body > div.common-container > div:nth-child(2) > div.wrap > ul > li:nth-child({}) > div > span.item_confirm'.format(i))
        Alls = Soup.select('body > div.common-container > div:nth-child(2) > div.wrap > ul > li:nth-child({}) > div > span.item_newconfirm'.format(i))
        Heals = Soup.select('body > div.common-container > div:nth-child(2) > div.wrap > ul > li:nth-child({}) > div > span.item_heal'.format(i))
        Deads = Soup.select('body > div.common-container > div:nth-child(2) > div.wrap > ul > li:nth-child({}) > div > span.item_dead'.format(i))
        for name,new,existing,all,heal,deal in zip(Names,News,Existings,Alls,Heals,Deads):
            result["地区"].append(name.text)
            result["新增"].append(new.text[4:])
            result["现有"].append(existing.text.split("较")[0])
            result["累计"].append(all.text)
            result["治愈"].append(heal.text)
            result["死亡"].append(deal.text)

df = pd.DataFrame(result)
pd.DataFrame(df).to_csv('result.csv')


