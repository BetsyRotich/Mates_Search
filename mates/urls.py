from django.contrib.auth import views as auth_views
from django.urls import path, include # new
from django.views.generic.base import TemplateView 
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),#handles login-page for user
    #path("account/profile/", views.profile, name="profile"),#handle request for profile-page for user
    #path("logout/", views.logout_user, name="logout"),#triggers logout for authenticated user
    #path("account/profile/:id"),#handles search for user in system

    path("register/", views.user_registration, name="register"),#handles user sign-up

    path("notifications/",views.notifications,name="notifications"),
    path("logout/", views.logout_user, name="logout"),

    path("notifications/", views.notifications, name="notifications"),
    path("discover/", views.discover, name="discover")
    # path("register/", views.user_registration, name="register")#handles user sign-up

]
