from django.apps import AppConfig


# Define the configuration for the 'library' application
class LibraryConfig(AppConfig):
    # Set the default auto field for model primary keys
    default_auto_field = 'django.db.models.BigAutoField'

    # Define the name of the Django application
    name = 'library'
