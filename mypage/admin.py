from django.contrib import admin
from .models import Diary, Calendar

# Register your models here.
admin.site.register(Diary)
admin.site.register(Calendar)