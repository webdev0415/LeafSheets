# Generated by Django 2.2.7 on 2019-11-14 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_auto_20191114_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='subtotal',
        ),
    ]