from django.shortcuts import render

def contact_view(request):
    contact_info={
        'phone':'+91 9876543210',
        'email':'contact@restaurant.com',
        'address':'123 Food Street, Bengaluru, Karnataka, India'
    }

    return render(request,'contact.html',{'contact_info':contact_info})