from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/',views.menu_list,name='menu_list'),
]