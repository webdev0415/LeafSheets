# Generated by Django 2.2.7 on 2019-11-15 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_auto_20191115_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingprofile',
            name='customer_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
