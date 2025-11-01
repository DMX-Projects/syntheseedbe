from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Career, JobApplication
from .serializers import CareerSerializer, JobApplicationSerializer


# ✅ Get all career opportunities
@api_view(['GET'])
def get_all_careers(request):
    """
    Fetch all career listings, ordered by most recently posted.
    """
    careers = Career.objects.all().order_by('-posted_on')
    serializer = CareerSerializer(careers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ Get a single career by ID
@api_view(['GET'])
def get_career_detail(request, pk):
    """
    Retrieve detailed information for a specific career by its ID.
    """
    try:
        career = Career.objects.get(pk=pk)
    except Career.DoesNotExist:
        return Response(
            {"error": "Career not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CareerSerializer(career)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ Apply for a specific Career
@api_view(['POST'])
def apply_for_career(request, pk):
    """
    Allows users to submit a job application for a specific career.
    """
    try:
        career = Career.objects.get(pk=pk)
    except Career.DoesNotExist:
        return Response(
            {"error": "Career not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    data = request.data.copy()
    data['career'] = career.id  # Associate the application with this career

    serializer = JobApplicationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Application submitted successfully!",
                "application": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
