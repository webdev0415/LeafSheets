# Generated by Django 2.2.7 on 2019-11-06 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '__first__'),
        ('leafsheets', '0010_auto_20191105_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='commerce.Item'),
        ),
    ]
