# Generated by Django 2.2.14 on 2021-05-26 21:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20210527_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ref_code',
        ),
        migrations.AlterField(
            model_name='item',
            name='data_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 5, 26, 21, 13, 49, 325928, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
