from django.apps import AppConfig

class BooksConfig(AppConfig):
    """
    Configuration class for the 'books' Django application.

    This class sets the default auto field type for models and defines
    the application name to be used in Django's app registry.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Defines the default field type for primary keys
    name = 'books'  # Specifies the name of the application
