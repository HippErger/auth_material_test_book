from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.views import serve

# Create your views here.

# def serve_docs(request):
#     return HttpResponse('Docs are going to be served here')

# def serve_docs(request, path):
#     return HttpResponse(path)

def serve_docs(request, path):
    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)
    return serve(request, path)