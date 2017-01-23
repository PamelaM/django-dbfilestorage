# Django-dbfilestorage

[![CircleCI](https://circleci.com/gh/tyrelsouza/django-dbfilestorage.svg?style=svg)](https://circleci.com/gh/tyrelsouza/django-dbfilestorage) [![codecov](https://codecov.io/gh/tyrelsouza/django-dbfilestorage/branch/master/graph/badge.svg)](https://codecov.io/gh/tyrelsouza/django-dbfilestorage)

Custom file storage for Django that stores file data and content type in the database.
Easy to use for testing when you don't care about a filename, and just want to test file data.

Intended to be used in tests, never in production.

## INSTALLATION

```
pip install django-dbfilestorage
```

Then in your project's `settings.py` file, add `'dbfilestorage'` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'dbfilestorage'
)
```

Next, if you want to set this globally, set the setting:

```python
DEFAULT_FILE_STORAGE='dbfilestorage.storage.DBFileStorage'
```

Or you can set it individually on a field: [Django Docs](https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.FileField.storage)

```python
from dbfilestorage.storage import DBFileStorage

class SomeClass(models.Model):
    file = models.FileField(upload_to=u'anywhere',
        storage=DBFileStorage())
```


## TODO

- More Tests
- Test that this works on a fake model, not just the storage file.
- Different django and different python versions.
- Store original filename in a field, maybe?
- Use original filename instead, so it honors the "upload_to" parameter.

## Signing Key
You can find my signing key at [TyrelSouza.com](https://tyrelsouza.com/blog/pgp-keys/)

I will sign everything with 0x769A1BC78A2DDEE2

## CHANGELOG

- 2017-01-23 [Tyrel Souza] Everything should return a "filename" even if it's generated. Make the filename be the hash + ext. (fall back to .txt)
- 2017-01-20 [Tyrel Souza] Make path return None if no file
- 2017-01-20 [Tyrel Souza] Make path return filename
- 2017-01-20 [Tyrel Souza] Add another migration, and redo all the initial migrations.
- 2017-01-20 [Tyrel Souza] Make sure migrations is actually there.
- 2017-01-20 [Tyrel Souza] Split filename and filehash.
- 2016-12-09 [Tyrel Souza] Add signing key to readme.
- 2016-12-09 [Tyrel Souza] Update Tests, add some cleanup.
- 2016-12-08 [Tyrel Souza] Add more documentation.
- 2016-12-07 [Tyrel Souza] Update Readme, move to github, gitlab wasn't functioning properly.
- 2016-12-07 [Tyrel Souza] Initial commits and basic project setup
