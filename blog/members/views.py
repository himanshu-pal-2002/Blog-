from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User




def register_user(request):
    if request.method == 'POST':
        un = request.POST['un']
        ps = request.POST["ps"]
        cps = request.POST['cps']
        if ps == cps:
            User.objects.create_user(username=un,password=ps).save()     
            return HttpResponseRedirect(reverse('login'))

    return render(request,'registration/registration.html')

def login_user(request):
    if request.method == 'POST':
        un = request.POST['un']
        ps = request.POST["ps"]
        user = User.objects.filter(username=un)
        if user:
            user = user[0]
            AOU = authenticate(username=un,password=ps)
            if AOU and AOU.is_active:
                login(request,AOU)
                
                return HttpResponseRedirect(reverse('home'))

    return render(request,'registration/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    

