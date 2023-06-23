from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'user'

urlpatterns = [
    path("login/", views.CustomLogin.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page="todolist:index"), name='logout'),
    path("signup/", views.SignUp.as_view(), name='signup'),
]