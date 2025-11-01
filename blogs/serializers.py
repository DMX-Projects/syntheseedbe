from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    read_more_url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'category', 'publish_date', 'summary', 'image_url', 'read_more_url']

    def get_read_more_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f"/api/blogs/{obj.slug}/")