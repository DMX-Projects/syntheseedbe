from rest_framework import serializers
from .models import Career, JobApplication


# ✅ Existing Career Serializer
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


# ✅ New Job Application Serializer
class JobApplicationSerializer(serializers.ModelSerializer):
    career_title = serializers.CharField(source='career.title', read_only=True)

    class Meta:
        model = JobApplication
        fields = [
            'id',
            'career',
            'career_title',
            'full_name',
            'email',
            'phone',
            'resume',
            'cover_letter',
            'applied_on',
        ]
        read_only_fields = ['applied_on']
