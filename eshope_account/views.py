from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.
from eshope_account.models import Profile


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method =='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email_phone=request.POST.get('email')
        password=request.POST.get('password')
        User.objects.create_user(first_name=firstname,last_name=lastname,username=email_phone ,email=email_phone, password=password)

        return redirect('/login')

    return render(request,'register.html',{})

def login_account(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method =='POST':
        email_phone=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(request , username=email_phone , password=password)
        if user is not None:
            login(request,user)
            return redirect("/")


    return render(request,"login.html",{})

def user_profile(request):
    user_id = request.user.id
    user_info = User.objects.get(id=user_id)
    profile_info = Profile.objects.get(user_id=user_id)

    context = {
        'userinfo': user_info,
        'profileinfo': profile_info
    }
    return render(request,'profile.html',context)

def user_profile_additional(request):
    user_id = request.user.id
    user_info = User.objects.get(id=user_id)
    profile_info = Profile.objects.get(user_id=user_id)
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        codemeli=request.POST.get('codemeli')
        phone=request.POST.get('phone')
        email=request.POST.get('email')

        user_info.first_name=firstname
        user_info.last_name=lastname
        user_info.email=email
        profile_info.phone=phone
        profile_info.code_meli=codemeli
        user_info.save()
        profile_info.save()
    context = {
        'userinfo': user_info,
        'profileinfo': profile_info
    }
    return render(request,'profile-additional-info.html',context)


def logout_account(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


    return render(request,'profile-additional-info.html',{})