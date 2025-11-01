from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ContactMessage
from .serializers import ContactMessageSerializer

import logging
logger = logging.getLogger(__name__)

# ---------------------------------------
# ✅ CONTACT FORM ENDPOINT (no change)
# ---------------------------------------
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


# ---------------------------------------
# 🧠 LOGIN ENDPOINT (NEW)
# ---------------------------------------
@csrf_exempt
@api_view(['POST'])
@authentication_classes([])  # disable default DRF auth
@permission_classes([AllowAny])  # allow anyone to log in
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"detail": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Try authenticating using email as username
    user = authenticate(request, username=email, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
