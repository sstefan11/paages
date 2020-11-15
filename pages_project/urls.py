# pages_project/urls.py
from django.contrib import admin
from django.urls import path, include # новое
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # новое
]

