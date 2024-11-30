
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path("register/", views.signup, name="register"),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("resend-otp", views.resend_otp, name="resend-otp"),
    path("login/", views.signin, name="signin"),
    path('logout/', views.customlogout, name ='logout'),
    path("home/",views.home,name="home"),
]
