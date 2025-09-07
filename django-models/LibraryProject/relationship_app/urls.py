from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import register, user_login, user_logout

urlpatterns = [
    path("books/", views.list_books, name="list_book"),  # FBV
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # CBV
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]


