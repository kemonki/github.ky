# Generated by Django 2.1.2 on 2020-10-22 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_item_sample_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sample_url',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='ホームページ'),
        ),
    ]