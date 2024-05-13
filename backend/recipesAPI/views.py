from django.http import JsonResponse
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# csrf_exempt decorator is used to disable a cookies error in Postman

# View to handle listing and creating new recipes
@csrf_exempt
@api_view(['GET', 'POST'])
def recipe_list(request):
    if request.method == 'GET':
        # Retrieve all recipes
        recipes = Recipe.objects.all()
        # Serialize the recipes data
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes': serializer.data})
    
    elif request.method == 'POST':
        # Create a new recipe based on the provided data
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# View to handle retrieving, updating, and deleting a specific recipe
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, id):
    try:
        # Get the specific recipe by its ID
        recipe = Recipe.objects.get(pk=id)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Retrieve and return the serialized data of the recipe
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Update the recipe data with the provided data
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)