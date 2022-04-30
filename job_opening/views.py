from django.shortcuts import render,redirect

# Create your views here.
# username admin password admin123@
def base(request):
    return render(request,"base.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")