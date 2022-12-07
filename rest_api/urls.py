from django.contrib import admin
from django.urls import path, include, re_path
from django.urls import re_path as urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]