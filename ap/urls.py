
from django.contrib import admin
from django.urls import path, include
from core import urls

urlpatterns = [
    path('site-manager/admin/', admin.site.urls),
    path("", include(urls)),
]
