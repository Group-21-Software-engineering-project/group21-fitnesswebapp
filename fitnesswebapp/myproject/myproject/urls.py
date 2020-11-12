"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home import views as home_views
from users import views as user_views
from bodyStats import views as bodyStats_views
from exercise import views as exercise_views
from foodTracker import views as foodTracker_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # home app views
    path('', home_views.home, name="home-page"),
    path('about/', home_views.about, name="about-page"),

    # users app views
    path('signup/', user_views.signUp, name="signUp-page"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login-page"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout-page"),
    path('profile/', user_views.profile, name="profile-page"),

    # bodyStats app views
    path('bodyStats/', bodyStats_views.bodyStats, name="bodyStats-page"),
    path('bodyStatsHistoryBMI/', bodyStats_views.bodyStatsHistoryBMI, name="bodyStatsHistoryBMI-page"),
    path('bodyStatsHistoryHeight/', bodyStats_views.bodyStatsHistoryHeight, name="bodyStatsHistoryHeight-page"),
    path('bodyStatsHistoryWeight/', bodyStats_views.bodyStatsHistoryWeight, name="bodyStatsHistoryWeight-page"),

    # exercise app views
    path('exercise/', exercise_views.exercise, name="exercise-page"),
    path('calendar/', exercise_views.CalendarView.as_view(), name="calendar-page"),
    path('form/', exercise_views.log, name="form-page"),
    path('form/(?p<exercise_log_id>\d+)/$',exercise_views.log, name="form-edit-page"),

    # food tracker app views
    path('foodTracker/', foodTracker_views.foodTracker, name="foodTacker-page"),

]