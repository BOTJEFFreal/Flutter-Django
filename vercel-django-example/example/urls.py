from django.urls import path
from .views import *

# Wire up our API using automatic URL routing.
urlpatterns = [
    
    path('add_api/images/', add_image, name='add_image'),
    path('api/images/<str:name>/', get_images, name='get_images'),

]