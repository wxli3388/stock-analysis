from django.db import models

# Create your models here.

class Stock_articles(models.Model):
    sid = models.AutoField(primary_key=True)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=70)
    publish_date = models.DateTimeField()
    article_url = models.CharField(max_length=60, unique=True)
    notification = models.CharField(max_length=1, default='N')

class Stock_data(models.Model):
    sid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    publish_date = models.DateField()
    trading_volume = models.IntegerField()
    turn_over = models.BigIntegerField()
    opening_price = models.DecimalField(max_digits=6, decimal_places=2)
    highest_price =models.DecimalField(max_digits=6, decimal_places=2)
    lowest_price = models.DecimalField(max_digits=6, decimal_places=2)
    closing_price = models.DecimalField(max_digits=6, decimal_places=2)
    change =  models.DecimalField(max_digits=6, decimal_places=2)
    transaction = models.IntegerField()
    last_bid_price = models.DecimalField(max_digits=6, decimal_places=2)
    last_ask_price = models.DecimalField(max_digits=6, decimal_places=2)
    price_earnings_ratio = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = (('code', 'publish_date'),)

class Stock_code(models.Model):
    sid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = (('code'),)