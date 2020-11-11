from django.urls import path
from . import views

from .views import DeveloperView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'developers', DeveloperView, 'developers')
urlpatterns = [
    path('', views.index, name=''),
    path('schedule', views.schedule, name='schedule'),
    path('products', views.products, name='products'),
    path('reports', views.reports, name='reports'),
] + router.urls