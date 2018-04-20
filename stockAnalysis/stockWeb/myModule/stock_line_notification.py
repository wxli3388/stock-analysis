import psycopg2
from psycopg2.extras import execute_values

import sys
import time

from datetime import datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage


try:
    author_white_list = ['lovdkkkk', 's10330076', 'MaInNine', 'q1w2e3r4t5']

    line_bot_api = LineBotApi('N8l3ZKewjdBmfplwDmh5j8K5uvaezW6J7Mpzv3wapa7v8dadamcZ/AKSXvADhiJaysBeINHzYCiDxmaz7eaZeQ2Cbrnpt1YIIS3Lfmm8Js+ZtfxzMKGc0RkWzVTDrX+Bf6wCmiCa098d3/XztWgyswdB04t89/1O/w1cDnyilFU=')

    conn = psycopg2.connect(database="stock", user="postgres", password="0921346555", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT sid,title,author,publish_date,article_url FROM stock_articles WHERE author = ANY(%s) AND notification = %s;",(author_white_list,'N'))
    rows = cur.fetchall()

    update_notification_id_list = []    
    for row in rows:        
        line_bot_api.push_message('C4032f45274917ee678af67b882dfc2f6', TextSendMessage(text=row[1]+'\n'+row[2]+'\n'+datetime.strftime(row[3], '%Y-%m-%d %H:%M:%S')+'\n'+row[4]))
        update_notification_id_list.append(row[0])
        time.sleep(1)

    
    cur.execute("UPDATE stock_articles SET notification = (%s) WHERE sid = ANY(%s);",('Y',update_notification_id_list))
    conn.commit()
    conn.close()

    sys.exit(0)

    """
    #raise Exception('證交所資料異常')
    """

        
except Exception as e:
    print(e)

