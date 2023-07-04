from django.urls import path
from .views import *

urlpatterns = [
    path('register/',SignupView.as_view(), name='signup'),
    path('protected/', MyProtectedView.as_view(), name='protected-view'),

]
