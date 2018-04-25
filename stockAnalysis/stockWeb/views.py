from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
        
    import sys
    from stockWeb.models import Stock_articles
    
    #sa = Stock_articles(author='test', title='test', publish_date='2018-04-24 00:00:00', notification='n')
    #sa.save()

    r = Stock_articles.objects.all()
    return HttpResponse(r[0].title)