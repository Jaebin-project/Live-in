from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Diary
from .forms import DiaryForm

def index(request):
    op_list = Diary.objects.order_by('id')
    form = DiaryForm()
    context = {'op_list':op_list, 'form':form,}
    return render(request, 'mypage/index.html', context)

@require_POST
def addResult(request):
    form = DiaryForm(request.POST)
    
    if form.is_valid():
        post = Diary(date = request.POST['date'],WBC = request.POST['wbc'],neutrophil = request.POST['neutrophil'],RBC = request.POST['rbc'],PT = request.POST['pt'],content = request.POST['comment'])
        post.save()
    
    return redirect('mypage')