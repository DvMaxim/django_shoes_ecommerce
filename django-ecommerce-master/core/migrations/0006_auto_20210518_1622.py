

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210518_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.CharField(choices=[('A', 'All'), ('M', 'Man'), ('W', 'Woman')], default='A', max_length=1),
        ),
    ]
