from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ("email", "username", "email", "birth", "pro")
