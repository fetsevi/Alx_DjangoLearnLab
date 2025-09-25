from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Book
from .serializers import BookSerializer

# List all open
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] # Read access for everyone
    
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
