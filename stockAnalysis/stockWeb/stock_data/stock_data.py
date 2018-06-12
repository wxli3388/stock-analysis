import os
import sys
import django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) # 将项目路径添加到系统搜寻路径当中
#os.environ['DJANGO_SETTINGS_MODULE'] = 'stockAnalysis.production_settings' # 设置项目的配置文件
os.environ['DJANGO_SETTINGS_MODULE'] = 'stockAnalysis.settings' # 设置项目的配置文件
django.setup()

import requests
import json
import datetime

from clear_string import *

from django.db import connection, transaction

class StockData():
    
    def get_stock_data(self, data_date=datetime.datetime.today().strftime('%Y%m%d')):
        
        # try:
            """
            #["0050","元大台灣50","4,099,855","1,127","336,213,829","82.25","82.35","81.80","82.10","<p style= color:green>-<\u002fp>","0.15","82.05","20","82.10","96","0.00"]
            #["證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比"]
            
            stock_data_json['data5'] =[["0050","元大台灣50","4,099,855","1,127","336,213,829","82.25","82.35","81.80","82.10","<p style= color:green>-<\u002fp>","0.15","82.05","20","82.10","96","0.00"],["0051","元大中型100","4,000","3","129,380","32.42","32.42","32.32","32.32"," ","0.00","32.16","50","32.32","3","0.00"]]

            0: stock_code 證券代號
            1: stock_name 證券名稱
            2: stock_trading_volume 成交股數
            3: stock_transaction 成交筆數
            4: stock_turn_over 成交金額
            5: stock_opening_price 開盤價
            6: stock_highest_price 最高價
            7: stock_lowest_price 最低價
            8: stock_closing_price 收盤價
            9, 10: stock_change 漲跌(+/-), 漲跌價差
            11: stock_last_bid_price 最後揭示買價
            13: stock_last_ask_price 最後揭示賣價
            15: stock_price_earnings_ratio 本益比
            
            """

            stock_date = data_date
            stock_date_hyphen = datetime.datetime.strptime(stock_date, '%Y%m%d').strftime('%Y-%m-%d')

            stock_api_response = requests.get('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=' + stock_date + '&type=ALL')
            stock_data_json = json.loads(stock_api_response.text)
            
            
            if stock_data_json['stat'] == 'OK':                    
                insert_list = []    
                clear_string_instance = ClearString()
                for row in stock_data_json['data5']:
                    if(row[5]=='--'):
                        continue

                    stock_change_symbol = clear_string_instance.clean_html(row[9])
                    if(stock_change_symbol=='+'):
                        stock_change_value = row[10].replace(',','')
                    elif(stock_change_symbol=='-'):
                        stock_change_value = 0-float(row[10].replace(',',''))
                    else:
                        stock_change_value = row[10].replace(',','')

                    if(row[11]=='--'):
                        stock_last_bid_price = 0.00
                    else:
                        stock_last_bid_price = row[11].replace(',','')
                    if(row[13]=='--'):
                        stock_last_ask_price = 0.00
                    else:
                        stock_last_ask_price = row[13].replace(',','')

                    one_stock_data = (
                        row[0], 
                        stock_date_hyphen, 
                        row[2].replace(',',''), 
                        row[3].replace(',',''), 
                        row[4].replace(',',''), 
                        row[5].replace(',',''), 
                        row[6].replace(',',''), 
                        row[7].replace(',',''), 
                        row[8].replace(',',''), 
                        stock_change_value, 
                        stock_last_bid_price, 
                        stock_last_ask_price, 
                        row[15].replace(',','')
                    )

                    cursor = connection.cursor()
                    cursor.execute('INSERT INTO "stockWeb_stock_data" (code, publish_date, trading_volume, transaction, turn_over, opening_price, highest_price, lowest_price, closing_price, change, last_bid_price, last_ask_price, price_earnings_ratio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (code,publish_date) DO NOTHING',one_stock_data)
                    cursor.execute('INSERT INTO "stockWeb_stock_code" (code, name) VALUES (%s, %s) ON CONFLICT (code) DO UPDATE SET name=(%s)',(row[0], row[1], row[1]))

            else:
                raise Exception('證交所資料異常')

        # except Exception as e:
        #     print(e)
            
        #print(stockDataJson['stat'])


if __name__ == "__main__":
    sd = StockData()
    sd.get_stock_data()
