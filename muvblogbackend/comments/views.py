from django.shortcuts import render
from .serializers import CommentSerializer
from .model import Comments
from rest_framework import viewsets

#creating comment view
class CommentViewSets (viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer