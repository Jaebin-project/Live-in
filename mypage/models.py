from django.db import models

# Create your models here.
class Diary(models.Model):
    # User_id = models.ForeignKey('User')
    date = models.DateField()
    title = models.CharField(max_length=20, default='no text')
    content = models.TextField(default="no text")
    EMOTION = [
        (1, '😍행복해요'),
        (2, '🙃보통이에요'),
        (3, '😑별로에요'),
        (4, '😭슬퍼요'),
        (5, '😡화나요'),
    ]
    emotion = models.IntegerField(default=2, choices=EMOTION)
    WBC = models.IntegerField(default=0)
    neutrophil = models.IntegerField(default=0)
    RBC = models.IntegerField(default=0)
    PT = models.IntegerField(default=0)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Calendar(models.Model):
    # User_id = models.ForeignKey('User')
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content