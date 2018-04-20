from django.db import models

# Create your models here.
class Stockk(models.Model):
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
