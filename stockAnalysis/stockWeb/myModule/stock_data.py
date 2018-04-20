import requests
import json

import psycopg2
from psycopg2.extras import execute_values

from fake_useragent import UserAgent

import datetime

import sys

from clear_string import *

#class StockData():
    
#    def getStockData(self):
        
try:
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

    stock_date = '20180301'
    stock_date_hyphen = datetime.datetime.strptime(stock_date, '%Y%m%d').strftime('%Y-%m-%d')

    stock_api_response = requests.get('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=' + stock_date + '&type=ALL')
    stock_data_json = json.loads(stock_api_response.text)
    
    
    if stock_data_json['stat'] == 'OK':                    
        insert_array = []    
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

            one_stock_data = (row[0], stock_date_hyphen, row[2].replace(',',''), row[3].replace(',',''), row[4].replace(',',''), row[5].replace(',',''), row[6].replace(',',''), row[7].replace(',',''), row[8].replace(',',''), stock_change_value, stock_last_bid_price, stock_last_ask_price, row[15].replace(',',''))
            insert_array.append(one_stock_data)

        conn = psycopg2.connect(database="stock", user="postgres", password="0921346555", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        execute_values(cur, 'INSERT INTO stockdata (stock_code, stock_date, stock_trading_volume, stock_transaction, stock_turn_over, stock_opening_price, stock_highest_price, stock_lowest_price, stock_closing_price, stock_change, stock_last_bid_price, stock_last_ask_price, stock_price_earnings_ratio) VALUES %s',insert_array)        
        conn.commit()
        conn.close()

    else:
        raise Exception('證交所資料異常')

        
except Exception as e:
    print(e)
#print(stockDataJson['stat'])



"""
ua = UserAgent()
print(ua.random)
"""

"""
import MySQLdb as mysql

conn = mysql.connect(host='localhost',port=3306,user='root',passwd='0921346555',db='stock',charset='utf8')
cursor = conn.cursor()
cursor.execute('SELECT * FROM stockdata LIMIT 10')
results = cursor.fetchall()

for row in results:
    print(row)

import psycopg2
conn = psycopg2.connect(database="stock", user="postgres", password="0921346555", host="127.0.0.1", port="5432")
print(conn)

"""