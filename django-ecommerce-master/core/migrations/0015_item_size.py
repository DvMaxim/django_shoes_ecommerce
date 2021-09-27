

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210521_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('1', 'XXL'), ('2', 'XL'), ('3', 'Large'), ('4', 'Medium'), ('5', 'Small')], default='1', max_length=1),
        ),
    ]
