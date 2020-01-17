from django.shortcuts import render, get_object_or_404
# import Blog object from models
from .models import Blog

def allblogs(request):
    # get all of the objects (jobs) from Job
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
