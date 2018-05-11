# coding=utf-8
import os
import sys
import django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'stockAnalysis.production_settings' # 设置项目的配置文件
django.setup()

import time

from datetime import datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage

from stockWeb.models import Stock_articles

try:
    author_white_list = ['lovdkkkk', 's10330076', 'MaInNine', 'q1w2e3r4t5']


    line_bot_api = LineBotApi('N8l3ZKewjdBmfplwDmh5j8K5uvaezW6J7Mpzv3wapa7v8dadamcZ/AKSXvADhiJaysBeINHzYCiDxmaz7eaZeQ2Cbrnpt1YIIS3Lfmm8Js+ZtfxzMKGc0RkWzVTDrX+Bf6wCmiCa098d3/XztWgyswdB04t89/1O/w1cDnyilFU=')

    rows = Stock_articles.objects.filter(notification='N').filter(author__in = author_white_list)

    update_notification_id_list = []
    for row in rows:
        update_notification_id_list.append(row.sid)

        #myline_id = 'U225d5f9dadad6cdfd1aa25a169228db2'
        #line_bot_api.push_message(myline_id, TextSendMessage(text=row.title+'\n'+row.author+'\n'+datetime.strftime(row.publish_date, '%Y-%m-%d %H:%M:%S')+'\n'+row.article_url))

        line_id = 'C4032f45274917ee678af67b882dfc2f6'        
        line_bot_api.push_message(line_id, TextSendMessage(text=row.title+'\n'+row.author+'\n'+datetime.strftime(row.publish_date, '%Y-%m-%d %H:%M:%S')+'\n'+row.article_url))
        time.sleep(1)
    line_bot_api.push_message(line_id, TextSendMessage(text="卡比丟到雲端測試"))

    Stock_articles.objects.filter(sid__in = update_notification_id_list).update(notification='Y')
    sys.exit(0)


    """
    #raise Exception('證交所資料異常')
    """

        
except Exception as e:
    print(e)

