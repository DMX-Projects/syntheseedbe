from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    read_more_url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'category',
            'summary', 'content', 'created_at',
            'image', 'read_more_url'
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_read_more_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f"/api/blogs/{obj.slug}/")
