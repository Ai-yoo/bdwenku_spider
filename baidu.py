# -*- coding: utf-8 -*-
'''
  author: duzhentong
  Date: 2019/1/21
  Time: 19:23
'''
import re

import requests
from bs4 import BeautifulSoup
import html
from html.parser import HTMLParser
from selenium import webdriver
import webbrowser
import uuid
from lxml import etree

def DOC(url):
    # if re.match('https://wenku.baidu.com/view/(.*).html.*',url):
    #     print('链接无效！')
    #     return
    doc_id = re.findall('view/(.*).html', url)[0]
    html = requests.get(url).text
    # title = etree.HTML(html.encode('utf-8')).xpath("//title/text()")[0].strip()
    # print(title)
    lists=re.findall('(https.*?0.json.*?)\\\\x22}',html)
    lenth = (len(lists)//2)
    # print(len(lists))
    # print(lenth)
    NewLists = lists[:lenth]
    for i in range(len(NewLists)) :
        NewLists[i] = NewLists[i].replace('\\','')
        txts=requests.get(NewLists[i]).text
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),',txts)
        for i in range(0,len(txtlists)):
            global y
            y=0
            if y != txtlists[i][1]:
                y = txtlists[i][1]
                n = '\n'
            else:
                n = ''
            filename = doc_id + '.txt'
            with open(filename,'a',encoding='utf-8') as f:
                f.write(n+txtlists[i][0].encode('utf-8').decode('unicode_escape','ignore').replace('\\',''))



print('请输入链接地址：')
url=input()
DOC(url)







