# Generated by Django 2.1.2 on 2020-10-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_item_sample_satisfaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='市区町村'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='都道府県'),
        ),
    ]
