from django.shortcuts import render
from django.conf import settings


def home_view(request):
    restaurant_name=getattr(settings,"RESTAURANT_NAME","Restaurant")
    return render(request,"home/index.html",{"restaurant_name":restaurant_name})

def about_view(request):
    restaurant_name=getattr(settings,"RESTAURANT_NAME","Restaurant")
    description=(
        "Welcome to {0}! We serve fresh, locally sourced food prepared with care. "
        "Our mission is to provide a warm dining experiance for families and friends. "
    ).format(restaurant_name)

return render(request,"home/about.html",{
    "restaurant_name":restaurant_name,
    "description":description,
})