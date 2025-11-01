from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Career
from .serializers import CareerSerializer


# ✅ Get all career opportunities
@api_view(['GET'])
def get_all_careers(request):
    careers = Career.objects.all().order_by('-posted_on')
    serializer = CareerSerializer(careers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ Get a single career by ID
@api_view(['GET'])
def get_career_detail(request, pk):
    try:
        career = Career.objects.get(pk=pk)
    except Career.DoesNotExist:
        return Response({"error": "Career not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CareerSerializer(career)
    return Response(serializer.data, status=status.HTTP_200_OK)