from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old ListAPIview endpoint
    path('books/', BookList.as_view(), name='book-list'), # Map to the BookList view
    
    # New ViewSet endpoint
    path('', include(router.urls)),
]
