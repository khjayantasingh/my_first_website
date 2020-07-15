from django import forms
from django.contrib.auth.models import User
from start_app.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    potfolio_url = forms.CharField(required = False)
    user_img = forms.ImageField(required = False)
    
    class Meta:
        model = UserProfile
        fields = ('user_img', 'potfolio_url')
