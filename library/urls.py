from django.urls import path
from .views import BookListCreateView, BookDetailView

# Define URL patterns for the books app
urlpatterns = [
    # URL for listing all books and creating a new book
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # URL for retrieving, updating, or deleting a specific book by its primary key (ID)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
