from django import forms
from django.contrib.auth.models import User

from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget= forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','email','password')


class userProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portofolio_site', 'profile_pic')

