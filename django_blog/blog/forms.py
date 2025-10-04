# Blog forms
from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    # comma-separated tags input
    tags = forms.CharField(
        required=False,
        help_text="Enter commat-seperated text(e.g. django, python, web).",
        widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3'})
        
    )
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your post content....'}),
            'tags': TagWidget(),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.isinstance and self.instance.pk:
            tag_qs = self.instance.tags.all().values_list('name', flat=True)
            self.fields['tags'].initial=', '.join(tag_qs)
            
    def _save_tags(self, instance):
        """
        Parse comma-separated tags from cleaned_data and assign them to the instance.
        """
        tag_str = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tag_str.split(',') if t.strip()]
        # get or create Tag objects
        tags = []
        for name in tag_names:
            tag_obj, _ = Tag.objects.get_or_create(name__iexact=name, defaults={'name': name})
            tags.append(tag_obj)
        # set M2M
        instance.tags.set(tags)

    def save(self, commit=True):
        # Save Post instance first, then handle tags
        instance = super().save(commit=commit)
        # if commit was False, instance won't have a pk yet; safe approach: ensure saved then set tags
        if not instance.pk:
            # if commit was False, save instance now to allow M2M assignment
            instance.save()
        self._save_tags(instance)
        return instance
    
    
    # Model comment form
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'write a comment'}),
    )
    
    class Meta:
        model = Comment
        fields = ['content']