from django import forms
from .models import Post
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        Model = Post
        fields = ('title', 'title_tag', 'author', 'body')
        
        widgets = {
            
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'})
        }
    