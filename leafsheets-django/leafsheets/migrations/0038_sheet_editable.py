# Generated by Django 2.2.8 on 2020-06-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leafsheets', '0037_auto_20200608_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='editable',
            field=models.BooleanField(default=True),
        ),
    ]
