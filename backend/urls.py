from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from content.views import homepage_view

urlpatterns = [
    path('', homepage_view, name='home'),  # Add a comma here
    path('admin/', admin.site.urls),
    path('api/', include('content.urls')),  # Include URLs from the content app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Correct the parameter name
