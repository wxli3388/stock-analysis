from django.db import models

# Create your models here.
"""
class Stock_data(models.Model):
    stockCode = models.CharField(max_length=10)
    stockDate = models.DateTimeField('date published')
    stockTradingVolume = models.IntegerField()
    stockTurnOver = models.IntegerField()
    stockOpeningPrice = models.FloatField()
    stockHighestPrice = models.FloatField()
    stockLowestPrice = models.FloatField()
    stockClosingPrice = models.FloatField()
    stockChange = models.FloatField()
    stockTransaction = models.IntegerField()
    stockLastBidPrice = models.FloatField()
    stockLastAskPrice = models.FloatField()
"""

class Stock_articles(models.Model):
    sid = models.AutoField(primary_key=True)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=70)
    publish_date = models.DateTimeField()
    article_url = models.CharField(max_length=60, unique=True)
    notification = models.CharField(max_length=1, default='N')
