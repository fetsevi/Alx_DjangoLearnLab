from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    
    #column to display in list view
    list_display = ('title', 'author', 'publication_year')
    
    #Add filter in the right sidebar
    list_filter = ('publication_year', 'author')
    
    #Add search functionality
    search_fields = ('title', 'author')
    
    #register with customization
admin.site.register(Book, BookAdmin)