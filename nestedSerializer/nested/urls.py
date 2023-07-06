from django.urls import path
from .views import *
urlpatterns = [
    path("basic/",current_datetime),
    path('nested/', NestedDataView.as_view()),
]