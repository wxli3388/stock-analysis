# coding=utf-8
import os
import sys
import django
sys.path.append('D:\codingProject\stockAnalysis\stockAnalysis') # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'stockAnalysis.settings' # 设置项目的配置文件
django.setup()


import requests

from bs4 import BeautifulSoup

from datetime import datetime

from stockWeb.models import Stock_articles


try:

    ptt_stock_url = 'https://www.ptt.cc/bbs/Stock/index.html'
    ptt_domain = 'https://www.ptt.cc'
    title_black_list = ['[公告]']
    
    response = requests.get(ptt_stock_url)
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('div', 'r-ent')

    url_list = []    
    for article in articles:
        
        if article.find('a'):   # 本文已被刪除 沒有 <a>
            article_url = article.find('a')['href']
            title = article.find('a').getText()

            if any(s in title for s in title_black_list):
                continue
                
            url_list.append(ptt_domain+article_url)

    article_upsert_list = []
    for one_url in url_list:
        response = requests.get(one_url)
        soup = BeautifulSoup(response.text, 'lxml')

        article_metas = soup.select('div.article-metaline > span.article-meta-value')
        
        if not article_metas:
            author = ''
            title = ''
            publish_date = None
        else:
            author = article_metas[0].getText().split()[0] #viger (瘋狂米哥) 去掉暱稱
            title = article_metas[1].getText() #[新聞] 美打壓陸電信業 衝擊鴻海台積電
            date = article_metas[2].getText() #'Thu Apr 19 08:30:00 2018'
            date_list = date.split()
            publish_date = datetime.strptime(date_list[2]+'-'+date_list[1]+'-'+date_list[4]+' '+date_list[3],'%d-%b-%Y %H:%M:%S')

        p = Stock_articles(author=author, title=title, publish_date=publish_date, article_url=one_url, notification='N')
        p.save()
        
        #article_upsert_list.append(Stock_articles(author=author, title=title, publish_date=publish_date, article_url=one_url, notification='N'))
    #Stock_articles.objects.bulk_create(article_upsert_list)    
    sys.exit(0)

except Exception as e:
    print(e)