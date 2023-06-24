from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import RecipesSerializer
from .models import Recipes

# Create your views here.
@api_view(['POST'])
def recipes(request):
    data = request.data
    recipes = Recipes.objects.create(
        recipe_name = data['recipe_name'],
        recipe_desc = data['recipe_desc'],
        recipe_img =  data['recipe_desc'])
    serializer = RecipesSerializer(recipes,many=False)
    return (Response(serializer.data))

@api_view(['GET'])
def getRecipes(request):
    recipes = Recipes.objects.all()
    serializer = RecipesSerializer(recipes,many = True)
    return(Response(serializer.data))
