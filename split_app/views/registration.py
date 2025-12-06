from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from split_app.serializers import UserRegistrationSerializer, UserResponseSerializer


class RegistrationView(APIView):
    def post(self, request):
        """
        Register a new user.
        Expected payload:
        {
            "username": "string",
            "email": "string",
            "password": "string"
        }
        """
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            response_serializer = UserResponseSerializer(user)
            return Response(
                {
                    "message": "User registered successfully",
                    "user": response_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
