from django.db import models

# The author model stores information about book authors

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# The Book model stores the book details and is linked to author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='Books', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
