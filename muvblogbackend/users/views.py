from django.shortcuts import render
from rest_framework import viewsets
from .model import UserProfile
from .serializers import UserProfileSerializer

#create user views
class UserProfileViewSets (viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
