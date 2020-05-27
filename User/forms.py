from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("ERROR : Password Is Wrong")
                )
        except models.User.DoesNotExist:
            self.add_error(
                "username", forms.ValidationError("ERROR : User Does Not Exist")
            )


class SignUpForm(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confrim Password")
    name = forms.CharField(max_length=20)
    pro = forms.BooleanField()

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError(
                "ERROR : User already exists with the same username"
            )
        except models.User.DoesNotExist:
            return username

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("ERROR : Password confirmation does not match")
        else:
            return password

    def save(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        name = self.cleaned_data.get("name")
        pro = self.cleaned_data.get("pro")

        user = models.User.objects.create_user(username, email, password)
        user.name = name
        user.pro = pro
        user.save()
