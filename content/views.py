# content/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Banner, Offer
from .serializers import BannerSerializer, OfferSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Banner View
@api_view(['GET'])
@permission_classes([AllowAny])
def get_banners(request):
    banners = Banner.objects.all()
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data)

# Offer View
@api_view(['GET'])
@permission_classes([AllowAny])
def get_offers(request):
    offers = Offer.objects.filter(is_active=True)
    serializer = OfferSerializer(offers, many=True)
    return Response(serializer.data)

# User Registration
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

# Login View
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

# Refresh Token View
class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)
