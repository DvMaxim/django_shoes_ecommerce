

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210520_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='subimage',
            name='title',
            field=models.CharField(default='Имя товара', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='sub_images',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubImage', verbose_name='Дополнительные картинки'),
        ),
        migrations.AlterField(
            model_name='subimage',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subimage',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subimage',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subimage',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
