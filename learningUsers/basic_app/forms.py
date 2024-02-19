from django import forms
from django.contrib.auth.models import User

from basic_app.models import UserProfileInfoForm


class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget= forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','email','password')


class userProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoForm
        fields = ('portofolio_site', 'profile_pic')

