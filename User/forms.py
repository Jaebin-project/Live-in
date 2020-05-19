from django import forms
from . import models


class LoginForm(forms.Form):

    name = forms.Charields()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


def clean(self):
    name = self.cleaned_data.get("name")
    password = self.clean_data.get("password")
    try:
        user = models.User.objects.get(username=name)
        if user.check_password(password):
            return self.cleaned_data
        else:
            self.add_error("password", forms.ValidationError("Password is Wrong"))
    except models.User.DoesNotExists:
        self.add_error("name", forms.ValidationError("Usere Does Not Exist"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("name", "email")
        widgets = "name" "email"
        password = forms.CharField(widget=forms.PasswordInput)
        password1 = forms.CharField(
            widget=forms.PasswordInput, label="Confirm Password"
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        try:
            models.User.objects.get(name=name)
            raise forms.ValidationError(
                "That name is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return name

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        name = self.cleaned_data.get("name")
        password = self.cleaned_data.get("password")
        user.username = name
        user.set_password(password)
        user.save()
