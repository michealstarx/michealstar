from django.shortcuts import render

from .models import Blog_post


def home_page(request):
    return render(request, 'star/home_page.html')

def blog_home(request):
    context = {
        'blogs': Blog_post.objects.all()
    }
    return render(request, 'star/blog_home.html', context)

def blog_details(request, id):
    context = {
        'blog': Blog_post.objects.get(id=id)
    }
    return render(request, 'star/blog_details.html', context)

def images(request):
    return render(request, 'star/images.html')