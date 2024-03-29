# Generated by Django 2.2.7 on 2019-11-14 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_auto_20191114_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('C', 'CREATED'), ('O', 'ORDERED'), ('R', 'REFUNDED')], default='C', max_length=1),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
