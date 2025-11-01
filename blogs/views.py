from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-publish_date')
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'