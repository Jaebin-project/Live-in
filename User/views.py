from django.views import View
from django.views.generic import FormView, DetailView
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms, models


class LoginView(FormView):
    template_name = "User/login.html"
    form_class = forms.LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    """def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return HttpResponse("Login Fail")
        return render(request, "User/login.html", {"form": form})
        """


def log_out(request):
    logout(request)
    return redirect("/")


class SignUpView(FormView):
    template_name = "User/signup.html"
    form_class = forms.SignUpForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class ProfileView(DetailView):
    model = models.User
