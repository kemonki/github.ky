# Generated by Django 2.1.2 on 2020-10-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_item_sample_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sample_cost',
            field=models.TextField(blank=True, max_length=10, null=True, verbose_name='値段'),
        ),
    ]
