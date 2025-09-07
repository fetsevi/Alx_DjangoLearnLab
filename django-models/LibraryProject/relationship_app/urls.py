from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path("books/", views.list_books, name="list_book"),  # FBV
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # CBV
]

