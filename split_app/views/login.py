from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)