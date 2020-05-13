from django.db import models

# Create your models here.
class Hospital(models.Model):
    ZONE_CATEGORY = [
        (1,'서울'),
        (2,'경기,인천'),
        (3,'강원'),
        (4,'충청'),
        (5,'경상'),
        (6,'제주'),
    ]
    name = models.CharField(max_length=20)
    zone = models.IntegerField(default=0, choices=ZONE_CATEGORY)
    info = models.TextField()
    site_url = models.URLField()
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=15)
    img = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    Hospital_id = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    SCORE = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]
    score = models.IntegerField(default=5, choices=SCORE)
    content = models.CharField(max_length=200)
    # User_id = models.ForeignKey('User')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:10]
