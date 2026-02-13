from rest_framework import serializers
from .model import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields= "_all_"

