# Generated by Django 5.1.7 on 2025-03-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration script for creating the 'Book' model in the database.

    This script initializes the 'Book' table with fields for storing
    book-related information such as title, author, published date, and ISBN.
    """

    initial = True  # Indicates that this is the initial migration for the app.

    dependencies = [
        # No dependencies, as this is the first migration for this model.
    ]

    operations = [
        # Creating the 'Book' model with its respective fields.
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                )),  # Auto-incrementing primary key
                ('title', models.CharField(
                    max_length=200
                )),  # Title of the book, limited to 200 characters
                ('author', models.CharField(
                    max_length=100
                )),  # Name of the book's author, limited to 100 characters
                ('published_date', models.DateField()
                ),  # Date when the book was published
                ('isbn', models.CharField(
                    max_length=13, unique=True
                )),  # ISBN number, must be unique
            ],
        ),
    ]
