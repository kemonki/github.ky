# Generated by Django 2.1.2 on 2020-10-28 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20201028_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
