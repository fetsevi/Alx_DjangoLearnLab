# Blog forms
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your post content....'}),
        }
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'write a comment'}),
    )
    
    class Meta:
        model = Comment
        fields = ['content']