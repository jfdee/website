from django.shortcuts import render
from .models import Developer
# Create your views here.


def render_main_template(request, template_name: str, someDict=None):
    """Render something template function"""
    return render(request, f'main/{template_name}', someDict)


def index(request) -> str:
    """Return template of main page and render it"""
    return render_main_template(request, 'index.html')


def schedule(request) -> str:
    """Return template of schedule page and render it"""
    return render_main_template(request, 'schedule.html')


def products(request) -> str:
    """Return template of products page and render it"""
    return render_main_template(request, 'products.html')


def developers(request) -> str:
    """Return template of developers page and render it"""
    developer_list = Developer.myManager.by_age('19')
    return render_main_template(request, 'developers.html', {'developer_list': developer_list})


def reports(request) -> str:
    """Return template of reports page and render it"""
    return render_main_template(request, 'reports.html')
