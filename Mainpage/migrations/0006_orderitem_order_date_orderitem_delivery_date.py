# Generated by Django 4.1.7 on 2023-03-20 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0005_reviewdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='Order_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='delivery_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]