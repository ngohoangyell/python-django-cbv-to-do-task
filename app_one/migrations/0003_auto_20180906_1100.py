# Generated by Django 2.1 on 2018-09-06 04:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20180906_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='ending_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 6, 4, 0, 56, 504423, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 6, 4, 0, 56, 504423, tzinfo=utc)),
        ),
    ]