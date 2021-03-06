# Generated by Django 2.0 on 2017-12-12 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20171212_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='claim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Claim'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
