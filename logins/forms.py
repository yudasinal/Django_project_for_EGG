from django import forms
from models import Info, CustomUser
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.forms import UserCreationForm

class InfoForm(forms.ModelForm):  

    class Meta:
        model = Info
        fields = ('organization_name', 'url', 'user_name', 'password', 'comments', 'department', 'game')


#CAN'T ADD GAME AND DEPARTMENT :(   
class MyRegistrationForm(UserCreationForm):         
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length = '200')
    last_name = forms.CharField(max_length = '200')
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    '''    
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']       
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.department = self.cleaned_data['department']
        user.set_password(self.cleaned_data['password1'])


    if commit:
        user.save()
            
        return user

    '''

    