from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('sign-in/', views.login_user, name='login'),
    path('sign-up/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name="logout"),
]