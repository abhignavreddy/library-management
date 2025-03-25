from django.db import models


# Define the Book model, representing a book entity in the database
class Book(models.Model):
    # Title of the book (maximum length: 200 characters)
    title = models.CharField(max_length=200)

    # Author of the book (maximum length: 100 characters)
    author = models.CharField(max_length=100)

    # Date when the book was published
    published_date = models.DateField()

    # ISBN number of the book (must be unique)
    isbn = models.CharField(max_length=13, unique=True)

    # String representation of the model, returns the book title
    def __str__(self):
        return self.title
