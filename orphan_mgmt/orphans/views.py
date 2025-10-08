from rest_framework import generics
from .models import Orphan, Course
from .serializers import OrphanSerializer, CourseSerializer

# ORPHANS CRUD

class OrphanListCreateView(generics.ListCreateAPIView):
    """Handles GET (list all orphans) & POST (create new orphan)"""
    queryset = Orphan.objects.all()
    serializer_class = OrphanSerializer
    
class OrphanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET single orphan, PUT (update), DELETE"""
    queryset = Orphan.objects.all()
    serializer_class = OrphanSerializer
    
# COURSES CRUD

class CourseListCreateView(generics.ListCreateAPIView):
    """Handles GET (list all courses) & POST (create new course)"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CourseDetailview(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET single course, PUT (update), DELETE"""
    queryset = Course.objects.all
    serializer_class = CourseSerializer
