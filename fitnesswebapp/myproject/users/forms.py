from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#creating a form with extra fields. ie email
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    password1 = forms.CharField(label='Enter Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            "username":None,
            "email":None,
            "password1":None,
            "password2":None,
        }

def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)


#update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            "username":None,
            "email":None,
        }
