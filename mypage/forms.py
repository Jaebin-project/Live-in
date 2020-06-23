from django import forms
from .models import Diary

EMOTION = (
    (1, '😍행복해요'),
    (2, '🙃보통이에요'),
    (3, '😑별로에요'),
    (4, '😭슬퍼요'),
    (5, '😡화나요'),
)

class DiaryForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'diary-date',}), label="오늘의 날짜 입력")
    wbc = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'diary-blood', 'placeholder':'백혈구 수치', }), label="혈액 수치 입력")
    neutrophil = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'diary-blood', 'placeholder':'중성구 수치', }), label="")
    rbc = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'diary-blood', 'placeholder':'헤모글로빈 수치', }), label="")
    pt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'diary-blood', 'placeholder':'적혈구 수치', }), label="")
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'diary-comment', 'placeholder':'간단히 오늘의 기분에 대해 적어보세요.', }))
    emotion = forms.ChoiceField(choices = EMOTION, label="오늘의 기분을 선택해주세요 : ", widget=forms.Select(attrs={'class':'diary-emotion'}))