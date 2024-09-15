# content/admin.py

from django.contrib import admin
from .models import Banner, Offer

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'discount', 'duration', 'is_active')
