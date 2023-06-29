
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from students.functions import handle_uploaded_file
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.http import Http404
import mimetypes


def index(request):
    
    return render(request,'index3.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        fname = request.POST.get('Firstname') #added this just now
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        enrollemnt = request.POST.get('Enrollment')

        checklist = [4117002020,717002020,35217002020,4517002020]

        if User.objects.filter(username = uname):
            messages.error(request,"Username already registered!!")
            return redirect('/')
        
        elif int(enrollemnt) not in checklist:
            messages.error(request,"you are not valid students")
            return redirect('register/')
        
        elif len(pass1) <=5:
            messages.error(request,"Use stronger Password")

        elif pass1 != pass2:
            messages.success(request,"your Password and Confirm Password don't match")
        
        else:
            my_user = User.objects.create_user(uname,email,pass2)
            # my_user = User.objects.create_user(uname,fname,email,pass2) # added fname just now
            my_user.save()
            messages.success(request, "your account has been successfuly created")
            return redirect("/")
    return render(request,"register1.html")

def SignUp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(username,pass1)

        user = authenticate(request,username = username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect('/home/')
              
        else:
            messages.success(request, ("* Invalid username or password "))
            return redirect('/')
        
    return render(request,'sign_up1.html')

def about(request):
    return HttpResponse("this is the about page!!")
        
def signout(request):
    # return HttpResponse("this is logout")
    logout(request)
    return redirect("/")
    # messages.success(request,"you successfully logout")

def year1(request):
    return render(request,'1year.html')

def year2(request):
    return render(request,'2year.html')

def year3(request):
    return render(request,'3year.html')

def report(request):
    return render(request,'report.html')
   
def uploadpage(request):
    if request.method =="POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = StudentForm()

    return render(request,'uploadpage.html',{'form':form})



def profile(request):
    return render(request,'Profile.html')


def attendence(request):
    return render(request,'attendence.html')


from django.http import FileResponse
import os

def download_file(request):
    # file_path = "E:\coding materials\portal\portals\static\media\attendence\CSS.pdf"  # Replace with the actual path to your file
    file_path = ""

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = FileResponse(f)
            response['Content-Disposition'] = 'attachment; filename="CSS.pdf"'
            return response

    # Handle the case where the file doesn't exist
    raise Http404("File not found")

def download_file1(request):
    # file_path = "E:\coding materials\portal\portals\static\media\attendence\CSS.pdf"  # Replace with the actual path to your file
    file_path = "E:\coding materials\portal\portals\static\media\fyear\BCASyllabusGGSIPU.pdf"

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = FileResponse(f)
            response['Content-Disposition'] = 'attachment; filename="BCASyllabusGGSIPU.pdf"'
            return response

    # Handle the case where the file doesn't exist
    raise Http404("File not found")

def download_file2(request):
    # file_path = "E:\coding materials\portal\portals\static\media\attendence\CSS.pdf"  # Replace with the actual path to your file
    file_path = "E:\coding materials\portal\portals\static\media\syear\HTML.pdf"

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = FileResponse(f)
            response['Content-Disposition'] = 'attachment; filename="HTML.pdf"'
            return response

    # Handle the case where the file doesn't exist
    raise Http404("File not found")

def download_file3(request):
    # file_path = "E:\coding materials\portal\portals\static\media\attendence\CSS.pdf"  # Replace with the actual path to your file
    file_path = "E:\coding materials\portal\portals\static\media\tyear\CSS.pdf"

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = FileResponse(f)
            response['Content-Disposition'] = 'attachment; filename="CSS.pdf"'
            return response

    # Handle the case where the file doesn't exist
    raise Http404("File not found")
      

# def download(request)
