from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomuserModel
        fields = ['username','email','display_name','user_type','password1','password2']

class AuthForm(AuthenticationForm):
    class Meta:
        model = CustomuserModel
        fields = ['username','password1']

class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfileModel
        fields = '__all__'
        exclude = ['user']

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfileModel
        fields = '__all__'
        exclude = ['user']


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPostModel
        fields = '__all__'
        exclude = ['user']
class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = '__all__'
        


