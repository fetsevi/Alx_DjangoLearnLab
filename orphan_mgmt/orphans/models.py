from django.db import models

# Orphans model 

class Orphan(models.Model):
    """Model to store orphan's personal information"""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True) # auto set when created
    
    def __str__(self):
        return self.name

# Courses model

class Course(models.Model):
   """Model to represent courses orphans can be enrolled in"""
   title = models.CharField(max_length=100)
   description = models.TextField()
   duration = models.IntegerField()
   
   def __str__(self):
       return self.title 
    
