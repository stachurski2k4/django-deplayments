from django import forms
from django.core import validators
from firstapp.models import Client,UserProfileInfo
from django.contrib.auth.models import User

def checkPass(value):
    for l in value:
        if(l==" "):
            raise forms.ValidationError("User name cannot have space i n it")

class Test(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    verify_password=forms.CharField(widget=forms.PasswordInput,label="Repeat your password")
    botcather=forms.CharField(required=False,
    widget=forms.HiddenInput,
    validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        data=super().clean()
        pass1=data['password']
        pass2=data['verify_password']

        if(pass1 != pass2):
            raise forms.ValidationError("Passwords don't match!")

    # def clean_botcather(self):
    #     botcather=self.cleaned_data['botcather']
    #     if(len(botcather)>0)
    #         raise forms.ValidationError('Gotcha bot!')
    #     return botcather

class NewUserForm(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')