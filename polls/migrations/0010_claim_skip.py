# Generated by Django 2.0 on 2017-12-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20171217_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='skip',
            field=models.IntegerField(default=0),
        ),
    ]