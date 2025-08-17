from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post
from .serializers import PostSerializer
from .filters import PostFilter


@method_decorator(cache_page(60), name="dispatch")  
class PostListCreateView(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "title", "author"]
    ordering = ["-created_at"]  

    def create(self, request, *args, **kwargs):
        
        return super().create(request, *args, **kwargs)



class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Exception:
           
            raise NotFound(detail="Post not found.")
