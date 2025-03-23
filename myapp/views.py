from django.shortcuts import render,redirect
from .models import Products
from django.contrib.auth import authenticate, login


# Create your views here.
def products_list(request):
    all_products = Products.objects.all()
    return render(request,'index.html',{'products' : all_products})

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('products_list')
        else:
            return render(request,'login.html',{'error':'Invalid Creds'})
        
    return render(request, 'login.html')