

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210519_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('high_boots', 'Сапоги'), ('boots', 'Ботинки'), ('half_boots', 'П/ботинки'), ('shoes', 'Туфли'), ('summer_shoes', 'Туфли летние'), ('home_shoes', 'Домашняя обувь'), ('sport_shoes', 'Обувь для активного отдыха')], max_length=26),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.CharField(choices=[('M', 'Man'), ('W', 'Woman'), ('U', 'Unisex')], default='U', max_length=1),
        ),
    ]
