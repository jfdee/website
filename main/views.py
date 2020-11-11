from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from main.logic.utils import *
from rest_framework import viewsets
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .serializers import DeveloperSerializer
from .models import Developer


class DeveloperView(viewsets.ModelViewSet):
    """Print developer list"""
    queryset = Developer.objects
    serializer_class = DeveloperSerializer


def render_main_template(request, template_name: str, context=None):
    """Render something template function"""
    return render(request, f'main/{template_name}', context)


def index(request) -> str:
    """Return template of main page and render it"""
    return render_main_template(request, 'index.html')


def schedule(request) -> str:
    """Return template of schedule page and render it"""
    return render_main_template(request, 'schedule.html')


@require_http_methods(["GET", "POST"])
def products(request):
    """Return template of products page and render it"""
    if request.method == "POST":
        file_object = request.data
        file_stream: bytes = file_object.read()
        file_object.seek(0)
        sha256 = get_hash_sha256(file_stream)
        sha1 = get_hash_sha1(file_stream)
        context = {'sha256': sha256, 'sha1': sha1}
        return JsonResponse(context, status=201)
    else:
        return render_main_template(request, 'products.html')

'''
def developers(request) -> str:
    """Return template of developers page and render it"""
    developer_list = Developer.myManager.find_developer(surname='Петров')
    return render_main_template(request, 'developers.html', {'developer_list': developer_list})
'''

def reports(request) -> str:
    """Return template of reports page and render it"""
    return render_main_template(request, 'reports.html')
