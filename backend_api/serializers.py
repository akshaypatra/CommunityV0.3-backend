from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ProfileInfo

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'college_name', 'state', 'city', 'enrollment_number', 'department', 'academic_year', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            college_name=validated_data['college_name'],
            state=validated_data['state'],
            city=validated_data['city'],
            enrollment_number=validated_data['enrollment_number'],
            department=validated_data['department'],
            academic_year=validated_data['academic_year'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class ProfileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileInfo
        fields = ['id', 'bio', 'skills', 'work', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
