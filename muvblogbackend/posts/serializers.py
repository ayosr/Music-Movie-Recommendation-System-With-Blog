from rest_framework import serializers
from .model import Posts
from comments.serializers import CommentSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = CommentSerializer (many=True, read_only=True)
    class Meta:
        model=Posts
        fields= "_all_"