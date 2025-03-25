from rest_framework.permissions import AllowAny
from .serializers import AdminSignupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.db.utils import IntegrityError

@permission_classes([AllowAny])
@api_view(["GET"])
def home_view(request):
    """
    Home endpoint providing basic API guidance.
    """
    return Response({
        "message": "Welcome to the Library Management System",
        "guidance": {
            "view_all_books": "/api/books/",
            "admin_signup": "/api/admin/signup/",
            "admin_login": "/api/admin/login/"
        }
    })


class AdminSignupView(APIView):
    """
    API endpoint to create an admin user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AdminSignupSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"message": "Admin registered successfully!"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {"error": "A user with this username or email already exists."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
