from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer
from .models import User
from django.core.exceptions import ValidationError

class SignupAPIView(APIView):
    
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            
            if User.objects.filter(username=username).exists():
                return Response({"error": "중복된 Username입니다."}, status=status.HTTP_400_BAD_REQUEST)
            
            if User.objects.filter(email=email).exists():
                return Response({"error": "이미 존재하는 email입니다."}, status=status.HTTP_400_BAD_REQUEST)
            
            user = serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)