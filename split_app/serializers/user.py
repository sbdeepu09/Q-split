from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from split_app.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles validation and password hashing automatically.
    """
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
        }
    
    def validate_username(self, value):
        """Validate that username is unique."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
    
    def validate_email(self, value):
        """Validate that email is unique and properly formatted."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    
    def create(self, validated_data):
        """Create a new user with hashed password."""
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.password = make_password(password)
        user.save()
        return user


class UserResponseSerializer(serializers.ModelSerializer):
    """
    Serializer for user response (excludes password).
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']
