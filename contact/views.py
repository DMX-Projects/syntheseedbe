from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import ContactMessage
from .serializers import ContactMessageSerializer

import logging
logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['POST'])
@authentication_classes([])           # No authentication required
@permission_classes([AllowAny])       # Allow public access
def submit_contact_form(request):
    print("🔥 submit_contact_form reached!")   # for debugging
    logger.debug("Received POST request to /api/contact/submit/")
    logger.debug(f"User: {request.user}, Auth: {request.auth}")

    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info("✅ Contact message saved successfully")
        return Response(
            {"message": "Message received successfully!", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
    else:
        logger.warning(f"❌ Invalid data: {serializer.errors}")
        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
