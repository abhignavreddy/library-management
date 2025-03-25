from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# Custom Pagination Class
class CustomPagination(PageNumberPagination):
    page_size = 5  # Default number of items per page
    page_size_query_param = 'page_size'  # Allows dynamic page sizing via query parameter
    max_page_size = 50  # Sets a limit to avoid excessive data fetching

# View for listing and creating books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer  # Use BookSerializer for serialization
    pagination_class = CustomPagination  # Apply pagination

    # Define permissions for different request methods
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]  # Allow anyone to view books
        return [IsAuthenticated()]  # Require authentication for adding books

    # Custom method to list books with sorting and pagination
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # Get all books

        # Get sorting parameter from request (default: sort by 'id')
        sort_by = request.GET.get("sort_by", "id").lower()

        # Restrict sorting to only 'id' or 'title' fields
        if sort_by not in ["id", "title"]:
            return Response({"error": "Invalid sort_by value. Choose 'id' or 'title'."}, status=400)

        # Apply sorting
        queryset = queryset.order_by(sort_by)

        # Apply pagination
        page = self.paginate_queryset(queryset)

        # Get page size dynamically (default to 5 if not provided)
        page_size = request.GET.get("page_size", "").strip()
        page_size = int(page_size) if page_size.isdigit() else 5

        # Prepare response data
        response_data = {
            "message": "List of all available books",
            "total_books": queryset.count(),
            "stats": {
                "books_per_page": page_size,
                "total_pages": (queryset.count() // page_size) + (1 if queryset.count() % page_size != 0 else 0),
                "sorted_by": sort_by  # Display the field used for sorting
            }
        }

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            response_data.update(paginated_response.data)  # Merge pagination details
            response_data["books"] = response_data.pop("results")  # Rename "results" to "books"
            return Response(response_data)

        serializer = self.get_serializer(queryset, many=True)
        response_data["books"] = serializer.data
        return Response(response_data)

# View for retrieving, updating, and deleting a book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer  # Use BookSerializer for serialization
    permission_classes = [IsAuthenticated]  # Require authentication for all actions

    # Custom delete method with a success message
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the book instance
        instance.delete()  # Delete the book
        return Response({"message": "Successfully deleted"}, status=status.HTTP_200_OK)
