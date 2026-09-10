from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status


class TestView(APIView):
    def get(self, request):
        return Response({"detail": "API Works!!!"}, status=status.HTTP_200_OK)
