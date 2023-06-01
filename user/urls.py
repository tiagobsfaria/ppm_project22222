from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user',views.logout_user, name="logout"),
    path('register_user',views.register_user, name="register_user"),
    path('user_information', views.user_data, name="user_data"),
    path('edit_user', views.edit_profile, name="edit_user"),
    path('password/', views.change_password, name="change_password"),
]
