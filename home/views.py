from django.shortcuts import render

def home_view(request):
    context={

        'restaurant_name':'Delicious Bites'
    }

    return render(request,'home.html',context)