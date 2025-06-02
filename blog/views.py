
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # faz login automático após cadastro
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})




def post_list_by_author(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author).order_by('-created_at')
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'filter_author': author,  # Passa o autor para o template
    })
