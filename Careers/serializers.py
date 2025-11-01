from rest_framework import serializers
from .models import Career

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = [
            'id',
            'title',
            'department',
            'location',
            'work_mode',
            'job_type',
            'description',
            'tags',
            'details',
            'posted_on',
        ]