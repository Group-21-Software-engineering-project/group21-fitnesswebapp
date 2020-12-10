from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm #imports django forms
from django.contrib import messages
from .forms import UserSignUpForm, UserUpdateForm
from django.contrib.auth.decorators import login_required #checks if users are logged in
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

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

#view for change profile data and checks if data is valid. If not data isnt saved
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-page')
            
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form':u_form
    }

    return render(request, 'users/profile.html', context)

#delete profile view
def deleteProfile(request, user_id = None):
    currentUser = get_object_or_404(User, pk=user_id) #get current user

    if request.method == 'POST':    #delete user and teturn to homepage
        currentUser.delete()
        messages.success(request, f'Account Successfully Deleted')
        return redirect('/')

    return render(request, 'users/profile.html', {'currentUser': currentUser}) #return to profile if method isnt POST

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile-page')