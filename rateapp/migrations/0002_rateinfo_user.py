# Generated by Django 2.2.11 on 2020-03-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateinfo',
            name='User',
            field=models.CharField(default='a', max_length=200),
        ),
    ]