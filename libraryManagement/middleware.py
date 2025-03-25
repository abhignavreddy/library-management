from django.http import JsonResponse

class CustomAuthMiddleware:
    """
    Middleware to handle unauthorized access (401 errors) globally.

    This middleware checks if the response status code is 401 and returns a JSON response
    with an appropriate error message instead of the default response.

    Attributes:
        get_response (callable): The next middleware or view in the request-response cycle.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware.

        Args:
            get_response (callable): The next middleware or view to process the request.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Processes the incoming request and checks for unauthorized access.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse or original response:
            - If the response status is 401, it returns a JSON response with an error message.
            - Otherwise, it returns the original response.
        """
        response = self.get_response(request)

        # Check if the response has a 401 status code and return a custom JSON response
        if response.status_code == 401:
            return JsonResponse({"error": "Unauthorized access. Please log in."}, status=401)

        return response
