from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path, inlude

urlpatterns = [
    path('',views.index,name='home'),
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('',include('home.urls'));
]
