from django.urls import path
from . import views

from main.views import DeveloperView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'developers', DeveloperView)
urlpatterns = [
    path('', views.index, name=''),
    path('schedule', views.schedule, name='schedule'),
    path('products', views.products, name='products'),
    path('reports', views.reports, name='reports'),
] + router.urls