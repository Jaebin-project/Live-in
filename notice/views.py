# from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BoardForm, CommentForm
from .models import Board, Comment

def index(request):
    boards = Board.objects
    return render(request, 'notice/index.html', {'boards': boards})

def boardform(request, board=None):
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.pub_date = timezone.now()
            board.save()
            return redirect('notice')
    else:
        form = BoardForm(instance=board)
        return render(request, 'notice/new.html', {'form': form})

def proboardform(request, board=None):
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.pub_date = timezone.now()
            board.pro = True
            board.save()
            return redirect('notice')
    else:
        form = BoardForm(instance=board)
        return render(request, 'notice/new.html', {'form': form})

def edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return boardform(request, board)

def remove(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('notice')

def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Board_id = board
            comment.content = form.cleaned_data['content']
            comment.pub_date = timezone.now()
            comment.save()
            return redirect('detail', board_id)
    else:
        form = CommentForm()
        return render(request, 'notice/detail.html', {'board': board, 'form': form})

def remove_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', comment.Board_id.id)