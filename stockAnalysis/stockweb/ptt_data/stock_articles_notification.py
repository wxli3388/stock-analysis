# coding=utf-8
import os
import sys
import django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'stockAnalysis.production_settings' # 设置项目的配置文件
#os.environ['DJANGO_SETTINGS_MODULE'] = 'stockAnalysis.settings' # 设置项目的配置文件
django.setup()

import time

from datetime import datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage

from stockweb.models import StockArticles

class PushNotification():
    
    def ptt_stock_push_line(self):
        try:
            author_white_list = ['lovdkkkk', 's10330076', 'MaInNine', 'q1w2e3r4t5', 'chengwaye']
            myline_id = 'U225d5f9dadad6cdfd1aa25a169228db2'
            line_id = 'C4032f45274917ee678af67b882dfc2f6'        

            line_bot_api = LineBotApi('N8l3ZKewjdBmfplwDmh5j8K5uvaezW6J7Mpzv3wapa7v8dadamcZ/AKSXvADhiJaysBeINHzYCiDxmaz7eaZeQ2Cbrnpt1YIIS3Lfmm8Js+ZtfxzMKGc0RkWzVTDrX+Bf6wCmiCa098d3/XztWgyswdB04t89/1O/w1cDnyilFU=')

            rows = StockArticles.objects.filter(notification='N').filter(author__in = author_white_list)

            update_notification_id_list = []
            for row in rows:
                update_notification_id_list.append(row.sid)
                
                #line_bot_api.push_message(myline_id, TextSendMessage(text=row.title+'\n'+row.author+'\n'+datetime.strftime(row.publish_date, '%Y-%m-%d %H:%M:%S')+'\n'+row.article_url))
                line_bot_api.push_message(line_id, TextSendMessage(text=row.title+'\n'+row.author+'\n'+datetime.strftime(row.publish_date, '%Y-%m-%d %H:%M:%S')+'\n'+row.article_url))
                time.sleep(1)

            StockArticles.objects.filter(sid__in = update_notification_id_list).update(notification='Y')
                
        except Exception as e:
            print(e)

# push_notification = PushNotification()
# push_notification.ptt_stock_push_line()