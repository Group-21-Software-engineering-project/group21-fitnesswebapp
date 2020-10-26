from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('', views.profile, name="profile-page"),
]