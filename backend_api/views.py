from rest_framework import generics,viewsets,status
from .serializers import CustomUserSerializer,ProfileInfoSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .models import ProfileInfo
from rest_framework.response import Response

from rest_framework.decorators import action

class UserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    

CustomUser = get_user_model()
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class ProfileInfoView(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]

    def list(self, request):
        profile = ProfileInfo.objects.filter(user=request.user).first()
        if profile:
            serializer = ProfileInfoSerializer(profile)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        ProfileInfo.objects.filter(user=request.user).delete()
        serializer = ProfileInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'], url_path='update')
    def update_profile(self, request):
        profile = ProfileInfo.objects.filter(user=request.user).first()
        if profile:
            profile.delete()
        serializer = ProfileInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='delete')
    def delete_profile(self, request):
        profile = ProfileInfo.objects.filter(user=request.user).first()
        if profile:
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)