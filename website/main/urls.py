from django.urls import path
from . import views


urlpatterns = [
    path ('home', views.index, name = 'home'),
    path ('schedule', views.schedule, name = 'schedule'), 
    path ('products', views.products, name = 'products'),
    path ('developers', views.developers, name = 'developers'),
    path ('reports', views.reports, name = 'reports'),
]