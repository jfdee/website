from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from main.views import DeveloperView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'developers', DeveloperView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include((router.urls, 'main'), namespace='instance_name')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
