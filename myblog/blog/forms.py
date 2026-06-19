from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6
            }),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment...'
            })
        }