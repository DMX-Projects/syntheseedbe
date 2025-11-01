from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog_list_api'),
    path('<slug:slug>/', BlogDetailAPIView.as_view(), name='blog_detail_api'),
]