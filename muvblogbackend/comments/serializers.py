from rest_framework import serializers
from .model import Comments

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model=Comments
        fields= "_all_"