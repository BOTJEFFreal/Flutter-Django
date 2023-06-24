from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRecipes),
    path('recipes/',views.recipes),
    ]

