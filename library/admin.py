from django.contrib import admin

# Import the Book model from the current app's models
from .models import Book

# Register the Book model with the Django admin site
# This allows the Book model to be managed through the Django admin interface
admin.site.register(Book)
