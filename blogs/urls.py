from django.urls import path, include
from . import views
urlpatterns = [
    path('home/',  views.home, name = "home"),
    
    path('blogs/blog',  views.blog, name = "blog"),
    path('search/',  views.search, name = "search"),
    
]