# content/urls.py

from django.urls import path
from .views import (
    get_banners,
    get_offers,
    register,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
)

urlpatterns = [
    path('banners/', get_banners, name='get_banners'),
    path('offers/', get_offers, name='get_offers'),
    path('register/', register, name='register_user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
