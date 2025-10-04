from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


# Model Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # used to redirect to post detail after create/edit
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    
# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_at"]
        
    def __str__(self):
       return f"comment by {self.author} on {self.post}"