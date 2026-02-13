from warnings import filters
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import viewsets, generics
from .serializers import PostSerializer
from .model import Posts
from .forms import PostForm
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

#creating comment view
class PostViewSets (viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

