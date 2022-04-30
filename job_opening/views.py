from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from job_opening.models import Companie
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
# username admin password admin123@
def base(request):
    return render(request,"base.html")

def login(request):
    if request.method=="POST":
        username= request.POST.get('loginName')
        password =  request.POST.get('loginPassword')
        record=Companie.objects.all();

        for i in range(len(record)):
            if check_password(password,record[i].salt) and username == record[i].username:
                print("yha a gaya")
                return redirect("/add")
        else:
            print("user not found")

    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        name=request.POST.get('registerName')
        username = request.POST.get('registerUsername')
        email = request.POST.get('registerEmail')
        password = request.POST.get('registerPassword')
        r_password =  request.POST.get('registerRepeatPassword')
        salt=make_password(password)
        if check_password(password,salt) and check_password(r_password,salt):
            company = Companie(name,username,email,salt)
            company.save()
            return redirect("/")
        else:
            print('invalid password and confirm password')

    return render(request,"register.html")

def add(request):
    return render(request,'add_button.html')

def addjobs(request):
    if request.method=="POST":
        jobRole = request.POST.get('jobRole')
        jobDesc = request.POST.get('jobDesc')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        print(jobRole,jobDesc,place,phone)

    return render(request,"add_job_opening.html")
