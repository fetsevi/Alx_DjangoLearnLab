from django.urls import path
from .views import (
    OrphanListCreateView, CourseListCreateView,
    OrphanDetailView, CourseDetailview
)

urlpatterns = [
    # Orphan endpoints
    path('orphans/', OrphanListCreateView.as_view(), name='orphan-list-create'),
    path('orphans/<int:pk>/', OrphanDetailView.as_view(), name='orphan-detail'),
    
    # Course endpoint
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailview.as_view(), name='course-detail')
]
