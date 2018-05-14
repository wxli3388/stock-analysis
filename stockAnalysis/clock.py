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


@sched.scheduled_job('interval', minutes=3)
def timed_job():
    sp = StockPtt()
    sp.get_articles()
    pn = PushNotification()
    pn.ptt_stock_push_line()

# def testing1():
#     print ("testing1 - every 2 min...")
#     sp = StockPtt()
#     sp.get_articles()
#     pn = PushNotification()
#     pn.ptt_stock_push_line()

# if __name__ == '__main__':
#     from apscheduler.schedulers.blocking import BlockingScheduler
#     sched = BlockingScheduler()
#     sched.add_job(testing1, 'cron', id='run_every_2_min', minute='*/2')

sched.start()