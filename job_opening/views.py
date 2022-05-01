from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from job_opening.models import NewJob
from django.contrib.auth import logout
from django.contrib import messages
import re
# username admin password admin123@

def base(request):
    return render(request,"base.html")

def login(request):
    if request.method=="POST":
        username= request.POST.get('loginName')
        password =  request.POST.get('loginPassword')
        user = auth.authenticate(username=username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/add")
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        name=request.POST.get('registerName')
        username = request.POST.get('registerUsername')
        email = request.POST.get('registerEmail')
        password = request.POST.get('registerPassword')
        r_password =  request.POST.get('registerRepeatPassword')
        reName = re.compile("[a-zA-Z]")
        match = re.match(reName,name)
        if (match is None):
            messages.warning(request,"For name use only alphabets")
        elif User.objects.filter(username=username).exists():
            messages.warning(request,"Username Taken")
        elif password !=r_password:
            messages.danger(request,"Password and confirm password didn't match!!!")
        elif User.objects.filter(email=email).exists():
            messages.warning(request,"Email Taken")
        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=name)
            user.save();
            messages.success(request,"User Created")
            return redirect("/")
    return render(request,"register.html")


def add(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'add_button.html')

def addjobs(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method=="POST":
        jobRole = request.POST.get('jobRole')
        jobDesc = request.POST.get('jobDesc')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        email = request.user.email
        rePhone = re.compile("[0-9]")
        if(re.match(rePhone,phone) is None):
            messages.warning(request,"Use only number in phone field")
        else:
            job = NewJob(email=email,jobRole=jobRole,jobDesc=jobDesc,place=place,phone=phone)
            job.save()
            messages.success(request,"Job Added")
            return redirect("/add")

    return render(request,"add_job_opening.html")
def logoutUser(request):
    logout(request)
    return redirect('/')
