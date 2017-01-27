from django.http import HttpResponse, Http404
from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import DBFile


def show_file(request, name):
    """
        Get the file object referenced by :name:
        Render the decoded base64 representation of the file,
            applying the content_type (or closest representation)

        :return HttpResponse: Rendered file
    """
    dbf = get_object_or_404(DBFile, name=name)
    response = HttpResponse(
        dbf.b64.decode('base64'),
        content_type=dbf.content_type)
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(
        dbf.name)
    return response
