# Generated by Django 2.2.9 on 2020-11-12 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_item_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='添付画像'),
        ),
    ]
