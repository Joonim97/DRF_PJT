from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer, UserSerializer
from .models import User


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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": '잘못된 아이디/비밀번호입니다.'}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileAPIView(APIView):

    permission_classes = [IsAuthenticated] 

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': '해당 유저를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user.username == username:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)