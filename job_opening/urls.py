from django.urls import path
from job_opening import views

urlpatterns = [
    # path("",views.base,name='base'),
    path("",views.login,name='login'),
    path("register",views.register,name='register'),
    path("add",views.add,name="add"),
    path("addjobs",views.addjobs,name="addjobs"),
    path('logout',views.logoutUser,name="logout"),
]