from django.contrib import admin
from django.urls import path
from students import views
# from .models import attendence
from .views import download_file,download_file1,download_file2,download_file3
from django_downloadview import ObjectDownloadView

# download = ObjectDownloadView.as_view(model= attendence,file_field= 'file')

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
    path('Attendence/',views.attendence,name='Attendence'),
    path('Profile/',views.profile,name='Profile'),
    path('download/', views.download_file, name='download_file'),
    path('download1/', views.download_file1, name='download_file1'),
    path('download2/', views.download_file2, name='download_file2'),
    path('download3/', views.download_file3, name='download_file3'),

   
    # path('download//',download,name='default'),
    # path('download/',views.download,name='download'),
   
]
