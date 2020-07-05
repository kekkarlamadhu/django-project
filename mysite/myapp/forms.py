from django import forms
from .models import UserData
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileForm(forms.ModelForm):

    class Meta():
         model = UserData

         fields = ('first_name','last_name','mobile','birth_date','profile_image',)
