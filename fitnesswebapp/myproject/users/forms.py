from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#creating a form with extra fields. ie email
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    #define passwords to remove the help text
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #removes help text from the body of the form. Its added under the ? icon
        help_texts = {
            "username":None,
            "email":None,
            "password1":None,
            "password2":None,
        }

def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

