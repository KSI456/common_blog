# Generated by Django 3.2 on 2021-07-10 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210710_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 10, 7, 41, 3, 399450, tzinfo=utc)),
        ),
    ]