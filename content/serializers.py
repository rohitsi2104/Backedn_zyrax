# content/serializers.py

from rest_framework import serializers
from .models import Banner, Offer

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'title', 'image', 'description']

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'title', 'amount', 'discount', 'duration', 'description', 'is_active']
