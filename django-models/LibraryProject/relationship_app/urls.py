from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books,
    LibraryDetailView,
    register,
    admin_view,
    librarian_view,
    member_view,
    add_book,       
    edit_book,      
    delete_book,    
)

urlpatterns = [
    path("books/", views.list_books, name="list_book"),  # FBV
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # CBV
     # Authentication
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    # Role-based access
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    # Book permissions views
    path("add_book/", add_book, name="add_book"),           
    path("edit_book/<int:pk>/", edit_book, name="edit_book"), 
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),
]


