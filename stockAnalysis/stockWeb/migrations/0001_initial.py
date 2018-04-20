# Generated by Django 2.0.3 on 2018-03-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stockk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockCode', models.CharField(max_length=10)),
                ('stockDate', models.DateTimeField(verbose_name='date published')),
                ('stockTradingVolume', models.IntegerField()),
                ('stockTurnOver', models.IntegerField()),
                ('stockOpeningPrice', models.FloatField()),
                ('stockHighestPrice', models.FloatField()),
                ('stockLowestPrice', models.FloatField()),
                ('stockClosingPrice', models.FloatField()),
                ('stockChange', models.FloatField()),
                ('stockTransaction', models.IntegerField()),
                ('stockLastBidPrice', models.FloatField()),
                ('stockLastAskPrice', models.FloatField()),
            ],
        ),
    ]
