from django.shortcuts import render
from .models import Developer
from main.logic.utils import *
# Create your views here.


def render_main_template(request, template_name: str, context=None):
    """Render something template function"""
    return render(request, f'main/{template_name}', context)


def index(request) -> str:
    """Return template of main page and render it"""
    return render_main_template(request, 'index.html')


def schedule(request) -> str:
    """Return template of schedule page and render it"""
    return render_main_template(request, 'schedule.html')


def products(request):
    """Return template of products page and render it"""
    if request.method == "POST":
        inputFile = request.FILES['file']
        sha256 = get_hash_sha256(inputFile.name)
        sha1 = get_hash_sha1(inputFile.name)
        context = {'fileName': inputFile.name, 'sha256': sha256, 'sha1': sha1}
        return render_main_template(request, 'products.html', context)
    else:
        return render_main_template(request, 'products.html')


def developers(request) -> str:
    """Return template of developers page and render it"""
    developer_list = Developer.myManager.by_surname('Садовников')
    return render_main_template(request, 'developers.html', {'developer_list': developer_list})


def reports(request) -> str:
    """Return template of reports page and render it"""
    return render_main_template(request, 'reports.html')
