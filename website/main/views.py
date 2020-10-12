from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def schedule(request):
    return render(request, 'main/schedule.html')

def products(request):
    return render(request, 'main/products.html')

def developers(request):
    return render(request, 'main/developers.html')

def reports(request):
    return render(request, 'main/reports.html')