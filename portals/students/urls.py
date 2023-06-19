from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path("home/",views.index, name='home'),
    path('about/',views.about, name='about'),
    path('register/',views.register,name='register'),
    path('',views.SignUp,name='SignUp'),
    path('SignOut/',views.signout,name='signout'),
    path('1year/',views.year1,name='1year'),
    path('2year/',views.year2,name='2year'),
    path('3year/',views.year3,name='3year'),
    path('report/',views.report,name='report'),
    path('uploadpage/',views.uploadpage,name='uploadpage'),
    path('ImageUpload/',views.Imageupload,name='Imageupload'),
   
]
