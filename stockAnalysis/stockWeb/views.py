# from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers
from datetime import datetime
from django.db.models.functions import Cast,TruncSecond
from django.db.models import DateTimeField,CharField

from stockWeb.models import Stock_articles


def ptt_stock_article(request):
            
    #row = Stock_articles.objects.filter(publish_date__gte=datetime.today().strftime('%Y-%m-%d')).values_list('title', 'author', 'article_url', 'publish_date')
    row = Stock_articles.objects.annotate(
            str_publish_date=Cast(
                TruncSecond('publish_date', DateTimeField()), CharField()
            )
        ).filter(
            publish_date__gte=datetime.today().strftime('%Y-%m-%d')
        ).values_list('title', 'author', 'article_url', 'str_publish_date')
    #print(row)
    # payload = serializers.serialize("json", row)
    # print(payload)
    
    return HttpResponse(row)