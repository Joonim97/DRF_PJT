from rest_framework import serializers
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # write_only -> 데이터를 받을 때만 사용
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'nickname', 'birth', 'gender']
        
    def create(self, validated_data):
            # 사용자 객체 생성
            user = User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
                email=validated_data['email'],
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
                nickname=validated_data.get('nickname', ''),
                birth=validated_data['birth'],
                gender=validated_data.get('gender', ''),
            )
            return user
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'nickname', 'birth', 'gender']