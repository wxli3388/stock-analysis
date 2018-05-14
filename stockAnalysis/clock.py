# coding=utf-8
import os
import sys
import django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'stockAnalysis.production_settings' # 设置项目的配置文件
#os.environ['DJANGO_SETTINGS_MODULE'] = 'stockAnalysis.settings' # 设置项目的配置文件
django.setup()

from stockWeb.ptt_data.get_stock_articles import StockPtt
from stockWeb.ptt_data.stock_articles_notification import PushNotification


from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=5)
def timed_job():
    sp = StockPtt()
    sp.get_articles(page_recursive=2)
    pn = PushNotification()
    pn.ptt_stock_push_line()

sched.start()