from rest_framework import serializers
from .models import Recipe, Ingredient, RecipeIngredient

# DB data needs to be serialized into native python data type

# Serializer for Ingredient model
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'category']

# Serializer for RecipeIngredient model
class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'measurement_unit']

    def create(self, validated_data):
        # Extract and create Ingredient data
        ingredient_data = validated_data.pop('ingredient')
        ingredient = Ingredient.objects.create(**ingredient_data)
        # Create RecipeIngredient with the associated Ingredient
        recipe_ingredient = RecipeIngredient.objects.create(ingredient=ingredient, **validated_data)
        return recipe_ingredient

# Serializer for Recipe model
class RecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'cooking_time', 'total_time', 'difficulty_level', 'recipe_ingredients']

    def create(self, validated_data):
        # Extract and create RecipeIngredient data
        recipe_ingredients_data = validated_data.pop('recipeingredient_set')
        recipe = Recipe.objects.create(**validated_data)
        # Create RecipeIngredients associated with the Recipe
        for recipe_ingredient_data in recipe_ingredients_data:
            recipe_ingredient_data['recipe'] = recipe
            RecipeIngredientSerializer().create(validated_data=recipe_ingredient_data)
        return recipe
