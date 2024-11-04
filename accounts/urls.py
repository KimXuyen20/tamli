from django.urls import path, include
from . import views
urlpatterns = [
    path('register/',  views.register, name = 'register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registerDoctor/', views.registerDoctor, name='registerDoctor'),
    path('accounts/edit/',  views.edit, name = "edit"),
]