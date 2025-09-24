from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer serializes the Book model fields and includes validation

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    # Custom validation to ensure publication year isn't in the future
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
# AuthorSerializer serializes Author fields and nets BookSerializer
# so that related books appear inline.

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many = True, read_only = True) # Nested serializer
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']