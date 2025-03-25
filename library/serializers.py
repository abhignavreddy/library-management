from rest_framework import serializers
from .models import Book

# Define a serializer for the Book model
# This serializer converts Book model instances to JSON and vice versa
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specify the model to serialize
        fields = '__all__'  # Includes all fields of the Book model
