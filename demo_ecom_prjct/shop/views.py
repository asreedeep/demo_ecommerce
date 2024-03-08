from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
def allproducts(request,p):
    c = Category.objects.get(name=p)
    p = Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})
def detail(request,p):
    p = Product.objects.get(name=p)
    return render(request,'detail.html',{'p':p})
def register(request):
    if (request.method == "POST"):
        n = request.POST['n']
        p = request.POST['p']
        cp = request.POST['cp']
        nf = request.POST['nf']
        nl = request.POST['nl']
        e = request.POST['e']
        if(p==cp):
            user = User.objects.create_user(username=n, password=p, first_name=nf, last_name=nl,email=e)
            user.save()
            return redirect('shop:allcategories')
        else:
            return HttpResponse("password same")
    return render(request, 'register.html')

def userlogin(request):
    if (request.method == 'POST'):
        n = request.POST['n']
        p = request.POST['p']
        user = authenticate(username=n,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcategories')
        else:
            return HttpResponse("invalid response")
    return render(request,'login.html')
@login_required
def userlogout(request):
    logout(request)
    return redirect('shop:login')

