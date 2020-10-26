from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #imports django forms

# Create your views here.
def signUp(request):
    form = UserCreationForm()
    return render(request, 'users/signUp.html',{'form': form})
