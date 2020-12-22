# Generated by Django 2.2.7 on 2019-11-05 05:13
"""

--- LeafSheets ---

Migrations — Leafsheets

Created on Wednesday, Oct 2, 2019
~ satyameva_jayate
"""

import os
import json
import urllib.request

from django.core.files import File
from django.db import migrations
from django.utils import timezone

from leafsheets.fixtures.sheets import SHEETS

# Migration

def create_sheets(apps, schema_editor):
    # We can't import the Sheet model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Sheet = apps.get_model('leafsheets', 'Sheet')
    for sheet in SHEETS:
        new_sheet = Sheet()
        new_sheet.created_at = timezone.now()
        new_sheet.updated_at = timezone.now()
        new_sheet.title = sheet['fields']['title']
        new_sheet.subtitle = sheet['fields']['subtitle']
        new_sheet.download_title = sheet['fields']['download_title']
        new_sheet.short_description = sheet['fields']['short_description']
        new_sheet.long_description = sheet['fields']['long_description']
        new_sheet.use_case = sheet['fields']['use_case']
        new_sheet.page_count = sheet['fields']['page_count']
        new_sheet.excerpt = sheet['fields']['excerpt']
        new_sheet.hours_saved = sheet['fields']['hours_saved']
        new_sheet.traditional_cost = sheet['fields']['traditional_cost']
        url = sheet['fields']['icon_url']
        result = urllib.request.urlretrieve(url)
        new_sheet.icon.save(
            os.path.basename(url),
            File(open(result[0], 'rb'))
            )
        new_sheet.save()

class Migration(migrations.Migration):

    dependencies = [
        ('leafsheets', '0006_auto_20191105_0502'),
    ]

    operations = [
        migrations.RunPython(create_sheets),
    ]
