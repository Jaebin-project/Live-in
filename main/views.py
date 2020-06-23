from django.shortcuts import render

def test(request):
    return render(request, 'main/test.html')

def login(request):
    return render(request, 'main/login.html')

def new_user(request):
    return render(request, 'main/new_user.html')