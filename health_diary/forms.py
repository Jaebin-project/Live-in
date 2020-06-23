from django import forms
from django.forms import TextInput, Textarea
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class':'floatLabel', 'placeholder':'Title'}),
            'content' : Textarea(attrs={'class':'floatLabel', 'placeholder':'Content'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content' : forms.TextInput(attrs={'class':'comment-content', 'placeholder':'댓글을 입력하세요.'}),
        }
        labels = {
            'content' : '',
        }