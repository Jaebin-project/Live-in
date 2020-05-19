from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    birth = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    pro = models.BooleanFiled()

    def __str__(self):
        return self.name
