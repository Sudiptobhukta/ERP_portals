from django.db import models
# from students.views import register
from django.contrib.auth.models import User

# Create your models here.

class report(models.Model):
    user = models.OneToOneField(User,null=False, on_delete=models.CASCADE,primary_key=True)
    yr1 =  models.FileField(upload_to="fyear/",null=True,blank=True)
    yr2 =  models.FileField(upload_to="syear/",null=True,blank=True)
    yr3 =  models.FileField(upload_to="tyear/",null=True,blank=True)

    def __str__(self):
        return self.user.username


class attendence(models.Model):
    file =models.CharField(max_length=10)
    file = models.FileField(upload_to="attendence/",null=True,blank=True)


class File(models.Model):
    username = models.CharField(max_length=10)
    filesave = models.FileField(upload_to="files/", null=True,blank=True)

    def __str__(self):
        return self.username



class student(models.Model):
    user = models.OneToOneField(User,null=False, on_delete=models.CASCADE,primary_key=True)
    First_name = models.CharField(max_length=122) 
    last_name= models.CharField(max_length=122)
    phone_number = models.CharField( max_length=12, null=True)
    Email = models.EmailField(max_length=254)
    # Password = models.CharField(max_length=50)
    student_image = models.ImageField(upload_to="media/",null=True,blank=True)
    # filesave = models.FileField(upload_to="files/", null=True,blank=True)
    ''' added later'''
    # student_subject = models.OneToOneField(subject,null=True,on_delete=models.CASCADE)


 

    def __str__(self):
        return self.user.username


