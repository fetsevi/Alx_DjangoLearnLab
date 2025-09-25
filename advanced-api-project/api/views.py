from rest_framework import generics, permissions, filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Book
from .serializers import BookSerializer

# List all open
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] # Read access for everyone
    
    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering options
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Search options
    search_fields = ['title', 'author__name']
    
    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # Default ordering
    
# Retreive a single Book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
# Create a new Book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # Only logged-in can create
    
# Update an existing Book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Allow only staff to update
    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only staff can update books.")
        serializer.save()
        
# Delete Book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
