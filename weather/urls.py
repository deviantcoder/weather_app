from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('remove-city/<str:pk>/', views.remove_city, name='remove_city'),
]