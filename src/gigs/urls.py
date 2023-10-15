from django.urls import path, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error/', views.error, name='error')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)