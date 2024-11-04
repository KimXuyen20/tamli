from django.urls import path, include
from . import views
urlpatterns = [
    path('chat/',  views.chat_view, name = "chat"),

    
]