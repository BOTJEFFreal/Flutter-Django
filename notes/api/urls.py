from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('notes/',views.getNotes),
    path('notes/<str:primaryKey>',views.getNote),
    path('notes/create/',views.createNote),
    path('notes/<str:primaryKey>/update/',views.updateNote),
    path('notes/<str:primaryKey>/delete/',views.deleteNote),
]