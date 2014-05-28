from django import forms
from models import Info, CustomUser
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.forms import UserCreationForm

# Form for adding a new information
class InfoForm(forms.ModelForm):  

    class Meta:
        model = Info
        fields = ('title', 'url', 'name', 'password', 'comments', 'department', 'game')

# Form to edit an existing information
class EditInfo(forms.ModelForm):  

    class Meta:
        model = Info
        fields = ('title', 'url', 'name', 'password', 'comments', 'department', 'game')

# Form to register a user  
class MyRegistrationForm(UserCreationForm):         
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length = '200')
    last_name = forms.CharField(max_length = '200')
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

  

    
