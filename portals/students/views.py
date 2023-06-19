
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from students.functions import handle_uploaded_file
from django.contrib.auth.decorators import login_required
from .forms import StudentForm,ImageForm
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage



def index(request):
   
    return render(request,'index3.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if User.objects.filter(username = uname):
            messages.error(request,"Username already registered!!")
            return redirect('/')
        
        elif len(pass1) <=5:
            messages.error(request,"Use stronger Password")

        elif pass1 != pass2:
            return HttpResponse("Your password and confirm password are not same!")
        
        else:
            my_user = User.objects.create_user(uname,email, pass2)
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

''' i temporarily commented the upload 
page from 92 to 100 '''
# def uploadpage2(request):  
#     context ={}
#     if request.method == "POST":
#         uploaded_file = request.FILES['myfile']
#         fs= FileSystemStorage()
#         name = fs.save(uploaded_file.name,uploaded_file)
#         context['url'] = fs.url(name)
#         print(uploaded_file.name)
#         print(uploaded_file.size)
#     return render(request,'uploadpage.html',context)
   
def uploadpage(request):
    if request.method =="POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = StudentForm()

    return render(request,'uploadpage.html',{'form':form})

def Imageupload(request):
    if request.method== 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = ImageForm()
    return render(request,'imageupload.html',{'form':form})

