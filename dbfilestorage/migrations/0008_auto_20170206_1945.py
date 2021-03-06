# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 19:45
from __future__ import unicode_literals

from django.db import migrations

def _fix_pk(apps, schema_editor):
    """ Set the primary_key to be a series """
    DBFile = apps.get_model("dbfilestorage", "DBFile")
    for idx, dbf in enumerate(DBFile.objects.all()):
        dbf.primary_key = idx+1
        dbf.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dbfilestorage', '0007_auto_20170206_1940'),
    ]

    operations = [
        migrations.RunPython(_fix_pk)
    ]
