from rest_framework import viewsets, permissions, filters, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom permission only the author can edit or delete"""
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author
        return obj.author==request.user
    
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all().order_by('-created_at')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Comment.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
# Feed functionality

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get users that the current user follows
        following_users = user.following.all()
        # Get posts only from followed users, ordered by newest first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


    
