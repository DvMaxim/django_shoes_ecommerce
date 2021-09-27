

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
