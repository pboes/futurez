# Generated by Django 2.0 on 2018-01-04 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20171227_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
