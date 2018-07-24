# from django.shortcuts import render

from django.core import serializers
from django.http import HttpResponse
from django.db.models.functions import Cast,TruncSecond
from django.db.models import DateTimeField,CharField
from django.db import connection, transaction
from django.core.paginator import Paginator

from datetime import datetime
import json
import sys

from .models import StockArticles,StockData,StockCode

def ptt_stock_article(request):
            
    qs = StockArticles.objects.annotate(
            publish_date_string=Cast(
                TruncSecond('publish_date', DateTimeField()), CharField()
            )
        ).values(
            'title', 'author', 'article_url', 'publish_date_string'
        ).order_by('-publish_date')

    if set(['keyword','column']).issubset(request.POST):
        if request.POST['column'] == 'title':
            qs = qs.filter(title__contains=request.POST['keyword'])
        if request.POST['column'] == 'author':
            qs = qs.filter(author__icontains=request.POST['keyword'])
            
    limit = 5
    if 'limit' in request.POST:
        limit = request.POST['limit']

    page = 1
    if 'page' in request.POST:
        page = request.POST['page']
    
    paginator = Paginator(qs, limit)
    data = paginator.get_page(page)

    result = {
        'statusCode':200,
        'payload' : {
            'data': list(data),
            'total': paginator.count
        }        
    }

    resultJson = json.dumps(result, ensure_ascii=False).encode('utf8')
    
    return HttpResponse(resultJson)

def stock_data(request):
    
    qs = StockData.objects.extra(
                select = {
                    'name': 'stockweb_stockcode.name'
                },
                tables = ['stockweb_stockcode'],
                where = ['stockweb_stockdata.code = stockweb_stockcode.code']
            ).filter(publish_date__gte='2018-07-17').values(
                'name','code','publish_date','trading_volume','transaction','turn_over','opening_price','highest_price','lowest_price','closing_price','change','last_bid_price','last_ask_price','price_earnings_ratio'
            ).order_by('-publish_date')

    if set(['keyword','column']).issubset(request.POST):
        if request.POST['column']=='code':
            qs = qs.filter(code__contains=request.POST['keyword'])
        elif request.POST['column']=='name':
            qs = qs.filter(name__contains=request.POST['keyword'])

    limit = 5
    if 'limit' in request.POST:
        limit = request.POST['limit']

    page = 1
    if 'page' in request.POST:
        page = request.POST['page']

    paginator = Paginator(qs, limit)
    data = paginator.get_page(page)
    
    data = [dict([a, str(x)] for a, x in b.items()) for b in data]
    
    result = {
        'statusCode':200,
        'payload' : {
            'data': list(data),
            'total': paginator.count
        }
    }

    resultJson = json.dumps(result, ensure_ascii=False).encode('utf8')    
    return HttpResponse(resultJson)

# def stock_data_raw(request):
    
#     cursor = connection.cursor()
#     select_sql = """SELECT sd.code,name,publish_date,trading_volume,transaction,turn_over,opening_price,highest_price,lowest_price,closing_price,change,last_bid_price,last_ask_price,price_earnings_ratio FROM "stockWeb_stock_data" sd LEFT JOIN "stockWeb_stock_code" sc ON sd.code=sc.code """
#     where_condition = """ WHERE 1=%s """
#     params = [1]

#     if set(['keyword','column']).issubset(request.POST):
#         if request.POST['column']=='code':
#             where_condition +=""" AND sd.code LIKE %s"""
#         else:
#             where_condition +=""" AND name LIKE %s"""
#         params.append("%"+request.POST['keyword']+"%")
#     select_sql += where_condition
#     where_list = copy.deepcopy(params)

#     limit = 10
#     if 'limit' in request.POST:
#         limit = request.POST['limit']
#     params.append(limit)

#     offset = 0
#     if 'page' in request.POST:
#         offset = (int(request.POST['page'])-1)*int(limit)
#     params.append(offset)
        
#     cursor.execute(select_sql+""" ORDER BY publish_date DESC,sd.sid ASC LIMIT %s OFFSET %s""", params)

#     row = dictfetchall(cursor)
#     data = [dict([a, str(x)] for a, x in b.items()) for b in row]
    
#     count_sql = """SELECT COUNT(1) FROM "stockWeb_stock_data" sd LEFT JOIN "stockWeb_stock_code" sc ON sd.code=sc.code"""
#     count_sql += where_condition
#     cursor.execute(count_sql,where_list)
#     total = cursor.fetchone()[0]

#     result = {
#         'statusCode':200,
#         'payload' : {
#             'data': data,
#             'total': total
#         }
#     }
#     resultJson = json.dumps(result, ensure_ascii=False).encode('utf8')
    
#     return HttpResponse(resultJson)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]