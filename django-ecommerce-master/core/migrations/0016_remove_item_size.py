# Generated by Django 2.2.14 on 2021-05-22 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_item_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
    ]