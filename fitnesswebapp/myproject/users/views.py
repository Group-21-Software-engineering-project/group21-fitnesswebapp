from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #imports django forms
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required #checks if users are logged in


# Create your views here.

#view for signUp validates form and sends sucess message + redirects to home page if sucessful
def signUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in!')
            return redirect('login-page')
    else:
        form = UserSignUpForm()
    return render(request, 'users/signUp.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
