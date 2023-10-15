from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.static import serve
from gigs.views import *
from django.conf import settings

urlpatterns = [
    path('', index, name='gigs_index'),
    path('confirm/', confirm_subscription, name='confirm_subscription'),
    re_path(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }),
    path('gigs/', include('gigs.urls')),
]
