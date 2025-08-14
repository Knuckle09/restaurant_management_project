from django.urls import path
from . import views
from .views import home_view

urlpatterns=[
    path('',views.homepage_view,name='homepage'),
    path('',home_view,name='home')
]