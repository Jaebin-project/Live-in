from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'notice-title', 'placeholder':'제목을 입력하세요.'}),
            'content' : forms.TextInput(attrs={'class':'notice-content', 'placeholder':'내용을 입력하세요.'}),
        }
        labels = {
            'title' : '',
            'content' : '',
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
