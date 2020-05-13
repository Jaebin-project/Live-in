from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Calendar
from .forms import TodoForm

def index(request):
    op_list = Calendar.objects.order_by('id')
    form = TodoForm()
    context = {'op_list' : op_list, 'form' : form,}
    return render(request, 'mypage/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Calendar(content=request.POST['text'])
        new_todo.save()

    return redirect('mypage')

def delete(request):
    Calendar.objects.all().delete()

    return redirect('mypage')

