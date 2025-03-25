from rest_framework import serializers
from django.contrib.auth.models import User

class AdminSignupSerializer(serializers.ModelSerializer):
    """
    Serializer for admin user registration.

    This serializer is used to validate and create a superuser (admin) account.
    It ensures that the password is write-only and has a minimum length requirement.
    """

    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        """
        Metaclass defining the model and fields used in the serializer.
        """
        model = User
        fields = ['username', 'email', 'password']  # Fields required for admin signup

    def create(self, validated_data):
        """
        Creates and returns a new superuser.

        Args:
            validated_data (dict): The validated user data containing username, email, and password.

        Returns:
            User: The newly created admin user.
        """
        # Create a superuser (admin account) using Django's built-in method
        user = User.objects.create_superuser(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
