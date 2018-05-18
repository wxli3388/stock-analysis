# from django.shortcuts import render

from django.core import serializers
from django.http import HttpResponse
from datetime import datetime
from django.db.models.functions import Cast,TruncSecond
from django.db.models import DateTimeField,CharField

import json

from stockWeb.models import Stock_articles


def ptt_stock_article(request):
            
    #row = Stock_articles.objects.filter(publish_date__gte=datetime.today().strftime('%Y-%m-%d')).values_list('title', 'author', 'article_url', 'publish_date')
    qs = Stock_articles.objects.annotate(
            publish_date_string=Cast(
                TruncSecond('publish_date', DateTimeField()), CharField()
            )
        ).filter(
            publish_date__gte=datetime.today().strftime('%Y-%m-%d')
        ).values(
            'title', 'author', 'article_url', 'publish_date_string'
        ).order_by('-publish_date')

    result = {
        'statusCode':200,
        'payload' : list(qs)
    }
    resultJson = json.dumps(result, ensure_ascii=False).encode('utf8')
    
    return HttpResponse(resultJson)