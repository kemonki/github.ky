# Generated by Django 2.1.2 on 2020-10-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201019_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sample_satisfaction',
            field=models.IntegerField(blank=True, null=True, verbose_name='満足度評価'),
        ),
    ]