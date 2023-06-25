from django.urls import path,include
from .views import fetch_all_images

urlpatterns = [
    # ... other URL patterns
    path('api/images/', fetch_all_images, name='fetch-all-images'),
]