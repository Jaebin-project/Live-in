# from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BoardForm
from .models import Board

def index(request):
    boards = Board.objects
    return render(request, 'notice/index.html', {'boards': boards})

def boardform(request, board=None):
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.pub_date = timezone.now()
            # 여기서 로그인한 사람이 전문가이면 board.pro를 True로 설정해주기!
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
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'notice/detail.html', {'board': board_detail})