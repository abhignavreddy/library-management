from django.http import JsonResponse

# Custom handler for 404 errors (Page Not Found)
def custom_404_handler(request, exception):
    """
    Handles 404 errors when a requested resource is not found.

    Args:
        request: The HTTP request object.
        exception: The exception raised when the resource is not found.

    Returns:
        JsonResponse: A JSON response with an error message and a 404 status code.
    """
    return JsonResponse({"error": "The requested resource was not found."}, status=404)

# Custom handler for 401 errors (Unauthorized Access)
def custom_401_handler(request, exception=None):
    """
    Handles 401 errors when a user tries to access a resource without authorization.

    Args:
        request: The HTTP request object.
        exception: (Optional) The exception raised for unauthorized access.

    Returns:
        JsonResponse: A JSON response with an error message and a 401 status code.
    """
    return JsonResponse({"error": "Unauthorized access. Please log in."}, status=401)
