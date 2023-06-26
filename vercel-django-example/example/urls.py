from django.urls import path
from .views import *

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('api/documents/', DocumentListCreateAPIView.as_view(), name='parent-list-create'),
    path('api/documents/<int:pk>/', DocumentRetrieveUpdateDestroyAPIView.as_view(), name='parent-retrieve-update-destroy'),
    path('api/images/', ImageListCreateAPIView.as_view(), name='child-list-create'),
    path('children/<int:pk>/', ImageRetrieveUpdateDestroyAPIView.as_view(), name='child-retrieve-update-destroy'),

]

