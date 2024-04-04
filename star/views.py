from django.shortcuts import render, redirect, reverse

from .models import Blog_post, Comment

from .comments import CommentForm

def home_page(request):
    return render(request, 'star/home_page.html')

def blog_home(request):
    context = {
        'blogs': Blog_post.objects.all()
    }
    return render(request, 'star/blog_home.html', context)

def blog_details(request, id):
    
    
    commentForm = CommentForm(request.POST or None)
    if commentForm.is_valid():
        commentForm.save()
        commentForm = CommentForm()
        
        return redirect(reverse('blog_details', kwargs={
            'id': id
        }))
    
    context = {
        'blog': Blog_post.objects.get(id=id),
        'commentForm': commentForm,
        'comments': Comment.objects.all()
    }
    return render(request, 'star/blog_details.html', context)

def images(request):
    return render(request, 'star/images.html')