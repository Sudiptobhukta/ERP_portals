from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm



class NewUserForm(UserCreationForm):
    
    email= forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ( "username", "email", "password1","password2")


    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class StudentForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    class Meta:
        model = File
        fields = ('username','filesave')
        labels = { 
            'name': '',
            'files': '',    
                        }
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = student
        fields= ('First_name','student_image')
        labels= {
            'name': '',
            'image': '',
        }
        

    


# class StudentForm(forms.ModelForm):
#     name = forms.CharField(label='Name', max_length=100)
#     files = forms.FileField()

# class StudentForm(ModelForm):
#     class Meta:
#         model = Customer
#         fields = ('First_name','files')
    

# class uploadForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     file = forms.FileField()
     
     
    
# class order_marksheet_Form(forms.ModelForm):
    
#     class Meta:
#         model = marksheet
#         fields = ("name","math")
