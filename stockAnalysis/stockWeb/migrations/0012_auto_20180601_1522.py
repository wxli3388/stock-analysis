# Generated by Django 2.0.3 on 2018-06-01 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockWeb', '0011_stock_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock_code',
            unique_together={('code',)},
        ),
    ]
