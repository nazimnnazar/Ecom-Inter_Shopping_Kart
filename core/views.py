
from email import message
from math import prod
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.
# def frontpage(request):
#     product=products.objects.all()
#     # categary=categ.objects.all()
#     return render(request,'index.html',{'pr':product})


def frontpage(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = products.objects.filter(category=c_page, available=True)
    else:
        prodt = products.objects.all().filter(available=True)
    cat = categ.objects.all()
    return render(request, 'index.html', {'pr': prodt, 'ct': cat})

def views(request,c_slug,product_slug):

    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'view.html',{'pr':prod})

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        message.success(request,"your account has been created")
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')
def servies(request):
    return render(request,'services.html')

def contact(request):
    return render(request, 'contact.html')