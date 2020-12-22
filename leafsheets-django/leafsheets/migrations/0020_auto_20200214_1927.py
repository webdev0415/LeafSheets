# Generated by Django 2.2.8 on 2020-02-14 19:27

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import leafsheets_django.utils


class Migration(migrations.Migration):

    dependencies = [
        ('leafsheets', '0019_company_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='doc',
        ),
        migrations.AddField(
            model_name='document',
            name='sheet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='doc', to='leafsheets.Sheet'),
        ),
        migrations.AddField(
            model_name='document',
            name='template_doc',
            field=models.FileField(default='a', upload_to=leafsheets_django.utils.PathAndRename('documents/docs/templates/')),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='variable_dict',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='variable_doc',
            field=models.FileField(blank=True, null=True, upload_to=leafsheets_django.utils.PathAndRename('documents/docs/variable/')),
        ),
        migrations.AddField(
            model_name='usersheet',
            name='doc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_sheets', to='leafsheets.Document'),
        ),
    ]
