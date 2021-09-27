

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210519_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.CharField(choices=[('A', 'All'), ('M', 'Man'), ('W', 'Woman'), ('U', 'Unisex')], default='U', max_length=1),
        ),
    ]
