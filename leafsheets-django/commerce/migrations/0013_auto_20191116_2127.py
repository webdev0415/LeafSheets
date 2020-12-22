# Generated by Django 2.2.7 on 2019-11-16 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0012_auto_20191115_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingprofile',
            name='addresses',
            field=models.ManyToManyField(blank=True, related_name='billing_profile_addresses', to='commerce.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_billing_addresses', to='commerce.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_shipping_addresses', to='commerce.Address'),
        ),
    ]
