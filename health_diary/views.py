from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post, Comment

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
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.Post_id = post_detail
                comment.content = form.cleaned_data['content']
                comment.pub_date = timezone.now()
                comment.save()
                return redirect('detail_hd', post_id)
        else:
            form = CommentForm()
            return render(request, 'health_diary/detail.html', {'post': post_detail, 'form': form})

# def edit_comment(request, comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     post = comment.Post_id
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.content = form.cleaned_data['content']
#             comment.pub_date = timezone.now()
#             comment.save()
#             return redirect('detail_hd', post.id)
#     else:
#         form = CommentForm(instance=comment)
#         return render(request, 'health_diary/detail.html', {'post': post, 'form': form})

def remove_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail_hd', comment.Post_id.id)
