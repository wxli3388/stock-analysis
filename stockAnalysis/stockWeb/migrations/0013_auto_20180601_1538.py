# Generated by Django 2.0.3 on 2018-06-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockweb', '0012_auto_20180601_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_data',
            name='publish_date',
            field=models.DateField(),
        ),
    ]
