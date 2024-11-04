from django.shortcuts import render

from blogs.models import Blog


def home(request):
    blogs = Blog.objects.all().filter(is_available=True)
    context={
        'blogs':blogs
    }
    return render(request,'home.html',context)