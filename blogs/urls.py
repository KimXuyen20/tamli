from django.urls import path, include
from . import views
urlpatterns = [
   
    
    path('blog/',  views.blog, name = "blog"),
    path('search/',  views.search, name = "search"),
    
]