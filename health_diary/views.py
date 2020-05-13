from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post

def index(request):
    posts = Post.objects
    return render(request, 'health_diary/index.html', {'posts': posts})

def postform(request, post=None):
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('health_diary')
    else:
        form = PostForm(instance=post)
        return render(request, 'health_diary/new.html', {'form': form})

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return postform(request, post)

def remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('health_diary')

def detail(request, post_id):
        post_detail = get_object_or_404(Post, pk=post_id)
        return render(request, 'health_diary/detail.html', {'post': post_detail})