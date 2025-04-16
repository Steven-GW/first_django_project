from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import logout

# Create your views here.
def posts_list(request):
    #posts = Post.objects.all().order_by('-date')
    posts = Post.objects.filter(user=request.user).order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug = slug)
    return render(request, 'posts/post_page.html', {'post': post})


def newpost(request):
    if (request.method == 'POST'):
        title = request.POST.get('title')
        body = request.POST.get('body')
        slug = request.POST.get('slug')
        ban = request.POST.get('postbanner')
        new_post = Post.objects.create(title=title, body=body, slug=slug, user=request.user)
        new_post.save()
        return redirect('posts:list')

    return render(request, "posts/newpost.html")


def logoutt(request):
    logout(request)
    return redirect('users:login')