from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='photos/blogs/')
    create_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.blog_name