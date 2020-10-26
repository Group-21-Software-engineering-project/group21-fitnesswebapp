from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #imports django forms
from django.contrib import messages
from .forms import UserSignUpForm


# Create your views here.

#validates form and sends sucess message + redirects to home page if sucessful
def signUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home-page')
    else:
        form = UserSignUpForm()
    return render(request, 'users/signUp.html',{'form': form})
