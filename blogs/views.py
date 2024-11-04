from django.shortcuts import render
from blogs.models import Blog
# Create your views here.


def blog(request):  

    blogs = Blog.objects.filter(is_available=True)
    
    context = {
        'blogs': blogs,
    }
    return render(request, 'blogs/blog.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            blogs = Blog.objects.order_by('create_date').filter(blog_name=keyword)

    context= {
        'blogs':blogs,
    }        

    return render(request,'blogs/blog.html', context)
