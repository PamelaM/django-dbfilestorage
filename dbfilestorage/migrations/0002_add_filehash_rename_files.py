# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 18:44
from __future__ import unicode_literals

from django.db import migrations, models

def copy_filehash(apps, schema_editor):
    DBFile = apps.get_model('dbfilestorage', 'DBFile')
    for dbf in DBFile.objects.all():
        dbf.filehash = dbf.name
        dbf.save()

def fix_filename(apps, schema_editor):
    DBFile = apps.get_model('dbfilestorage', 'DBFile')
    for dbf in DBFile.objects.all():
        ext = dbf.content_type.split("/")[0]
        dbf.name = "{name}.{ext}".format(
            name=dbf.name,
            ext=ext)
        dbf.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dbfilestorage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbfile',
            name='filehash',
            field=models.CharField(default='filehash', max_length=32, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dbfile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.RunPython(copy_filehash),
        migrations.RunPython(fix_filename),
    ]