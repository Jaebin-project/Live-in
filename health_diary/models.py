from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # User_id = models.ForeignKey('User')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    Post_id = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    # User_id = models.ForeignKey('User')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]