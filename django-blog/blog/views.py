from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django import forms

# Simple form for creating posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

